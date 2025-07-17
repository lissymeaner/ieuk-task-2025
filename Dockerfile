# Dockerfile, Image, Container

# 1. Define language and author of application
FROM python:latest
LABEL authors="afuwa"



# 2. Add main program
ADD app/main_program.py .

# 3. Run all libraries
RUN pip install FastAPI uvicorn Jinja2 MarkupSafe Werkzeug blinker click colorama itsdangerous pip

# 4. Dockerise app
CMD ["python", "./main.py"]