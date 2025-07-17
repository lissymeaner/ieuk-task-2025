# Engineering project
A FastAPI-powered application that checks the log IPs against the top 16 bot IPs, and then sends either a "welcome" message or a "503 error" depending on the client IP.

## For users
1. Extract the zip folder from your file directory.
2. Open your terminal, and change the current directory to ``[your path here]/ieuk-task-2025-main``.
3. Activate the virtual environment for the program.
4. Change the app
5. Run the server and start the application with ``uvicorn main_program:app --reload``
6. If your IP is not one of the top 16, then a "Welcome" message will show up on the screen

## How to activate the virtual environment

### Command lines
1. Use ``python -m venv venv`` or ``python3 -m venv venv``
2. Line to activate:

    | Operating System (OS) | Code |
    |-----------------------|------|
    |Windows                |``./venv/Scripts/activate``|
    |Linux                  |source venv/bin/activate|
    |Mac                    |source ./venv/bin/activate|

## To further verify
Spoof the top 16 IPs as client IPs.

## For devs: what to fix
1. Display a welcome message for all pages instead of just the index page