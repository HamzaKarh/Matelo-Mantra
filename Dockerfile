# base image
FROM python:3.9
# setup environment variable
ENV DockerHOME=/

# set work directory
RUN mkdir -p $DockerHOME

# where your code lives
WORKDIR $DockerHOME

ADD . /

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
# copy whole project to your docker home directory. COPY . $DockerHOME
# run this command to install all dependencies
RUN pip install -r requirements.txt

RUN python manage.py migrate

# port where the Django app runs
EXPOSE $PORT
# start server
CMD python manage.py runserver