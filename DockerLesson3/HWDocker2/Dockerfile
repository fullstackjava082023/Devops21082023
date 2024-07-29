# Use the official Python base image
FROM python:3.12-slim 

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
ADD . /app

# Run the Python script
ENTRYPOINT ["python" ,"print_time.py"]

