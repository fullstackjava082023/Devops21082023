FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
# COPY . /app
COPY main.py /app/main.py


# on docker run, execute the python script
CMD ["python", "main.py"]
