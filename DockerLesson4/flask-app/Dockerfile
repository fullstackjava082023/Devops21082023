# from python
FROM python:3.12-slim

# set the working directory in the container
WORKDIR /app

# copy current directory to the container
ADD . /app

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start after 10 sec sleep in the entrypoint
ENTRYPOINT [ "python", "app.py" ]

