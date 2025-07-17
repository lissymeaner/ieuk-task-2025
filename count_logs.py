import re
from collections import Counter

# From stack overflow
def get_ips(fname):
    # a pattern to match IPv4
    ip_re = re.compile(r'^\s*(\d+\.\d+\.\d+\.\d+)')
    with open(fname, encoding="utf-8") as file:
    # for each line in the file
      for line in file:
        ip_match = ip_re.search(line) # pass the line
        # extract the IP, or ignore if it does not have an IP
        if ip_match is not None:
          # group(131251) is the pattern in parenthesis, the ip.
          yield ip_match.group(1)

# Researched using W3Schools


def count_logs():
    log = open("./sample-log.log", "rt")
    logs = log.readlines()
    number_of_logs = len(logs)

    log.close()

    print(str(number_of_logs))


count_logs()

ips = Counter(get_ips("sample-log.log"))
most_frequent_ips = ips.most_common(20) # gets the 20 more frequent IPs

print(most_frequent_ips)