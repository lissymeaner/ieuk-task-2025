# Engineering project
A FastAPI-powered application that checks the log IPs against the top 16 bot IPs, and then sends either a "welcome" message or a "503 error" depending on the client IP.

## For users
1. Extract the zip folder from your file directory.
2. Open your terminal, and change the current directory to ``[your path here]/ieuk-task-2025-main``.
3. Activate the virtual environment for the program.
4. Ensure [pip](https://pypi.org/project/pip/), [FastAPI](https://fastapi.tiangolo.com/), [uvicorn](https://pypi.org/project/uvicorn/), [Jinja2](https://pypi.org/project/jinja2/), [MarkupSafe](https://pypi.org/project/markupsafe/), [Werkzeug](https://pypi.org/project/werkzeug/), [blinker](https://pypi.org/project/blinker/), [click](https://pypi.org/project/click/), [colorama](https://pypi.org/project/colorama/), and [itsdangerous](https://pypi.org/project/itsdangerous/) are installed.
5. Change the directory to the app folder
6. Run the server and start the application with ``uvicorn main_program:app --reload``
7. If your IP is not one of the top 16, then a "Welcome" message will show up on the screen

## How to activate the virtual environment

### Command lines
1. Use ``python -m venv venv`` or ``python3 -m venv venv``
2. Line to activate:

    | Operating System (OS) | Code |
    |-----------------------|------|
    |Windows                |``./venv/Scripts/activate``|
    |Linux                  |source venv/bin/activate|
    |Mac                    |source ./venv/bin/activate|

## For devs:
### What to fix
Display a welcome message for all pages instead of just the index page
### To further verify:
Spoof the top 16 IPs as client IPs.
