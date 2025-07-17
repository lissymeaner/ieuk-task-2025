# libraries
from fastapi import FastAPI, Request, Response
import re
import sys
from pathlib import Path
import collections

# ------------------------------------------------------------------------------------
# ----------------------------------- Functions --------------------------------------
#-------------------------------------------------------------------------------------


# ------------------------------- Finding top IPs ------------------------------------
# ----------------------------- From stack overflow ----------------------------------
# --------------------------- a pattern to match IPv4 --------------------------------

ip_re = re.compile(r'^\s*(\d+\.\d+\.\d+\.\d+)')

def top_ips(fname: Path, limit: int = 16):
    counter = collections.Counter()

    # Stream line-by-line: constant memory
    with fname.open('r', encoding="utf-8", errors='ignore') as file:
    # for each line in the file
      for line in file:
        ip_match = ip_re.search(line) # pass the line
        # extract the IP, or ignore if it does not have an IP
        if ip_match is not None:
          counter[ip_match.group(1)] += 1

    return counter.most_common(limit)

#-------------------------------- APP CREATION ---------------------------------------
def create_app(blocked_ips: set) -> FastAPI:
    app = FastAPI()

    @app.middleware("http")
    async def block_suspicious(request: Request, call_next):
        if request.client.host in blocked_ips:
            # log to stdout for visibility
            return Response(status_code= 503, content="503 Error for suspicious IP")
        return await call_next(request)

    @app.get("/", include_in_schema=False)
    async def index():
        return {"message":"Welcome!"}

    return app


#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

log_file = Path(sys.argv[1]) if len(sys.argv) == 2 else Path("../sample-log.log")
if not log_file.exists():
    top16 = top_ips(log_file)
    blocked_set = {ip for ip, _ in top16}
else:
    top16 = []
    blocked_set = set()

if top16:
    print("Top 16 suspicious IPs (by request count):")
    for ip, hits in top16:
        print(f"{ip:<15}   {hits:>7}")

# Create the app
app = create_app(blocked_set)

#-------------------------------------------------------------------------------------
#--------------------------------- MAIN PROGRAM --------------------------------------
#-------------------------------------------------------------------------------------

def main() -> None:
    # Run from CLI just to list suspicious IPs.
    if len(sys.argv) != 2:
        print("Usage: python main_program.py ../sample-log.log")
        sys.exit(1)

    # Run the app
    print("\nRun the server with:\n uvicorn main_program:app --reload")

if __name__ == "__main__":
    main()
