# from python
FROM python:3.12-slim

# set the working directory in the container
WORKDIR /app

# copy current directory to the container
ADD . /app

# install dependencies
RUN pip install -r requirements.txt


# using wait for it script for MYSQL connection
# ENTRYPOINT ["wait-for-it.sh", "db:3306", "--", "python", "app.py"]

## Add a sleep command to delay execution
#ENTRYPOINT ["sh", "-c", "sleep 10 &&  python app.py"]

# command to run on container start after 10 sec sleep in the entrypoint
ENTRYPOINT [ "python", "app.py" ]

