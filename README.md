# assignment2-ss1078
This is for assignment 2 for ece 590 (simplified version)


## What does the app do?
It counts the number of page visits on a given web page. The page when loaded looks like:

![demo app](https://github.com/srishtis/assignment2-ss1078/blob/master/assignment2-ss1078.PNG)


## How did I create the dockerized version of the app?

The Dockerfile created had the following content:

```
FROM python:3.5-alpine
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["python", "app.py"]
```

The docker image was built and pushed (was first built in gcp- you can also do it directly) using the following commands. To push it to dockerhub you will need to create your account and login to it (using ```docker login```):

```
docker build -t gcr.io/assignment2-ss1078/assignment2-ss1078:v2 .
docker tag gcr.io/assignment2-ss1078/assignment2-ss1078:v2 ss2809/assignment2-ss1078
docker push ss2809/assignment2-ss1078
```

Then, you can simply pull the image and run it using the instructions below.

## How to run the app
The app is already packaged with a Dockerfile which sets and configures the environment. The docker-compose.yml file sets and configures the services for the flask app: both python and redis (as redis is being used for counting the page visits).

### Steps:

1. Clone the repository using (optional): 

```
git clone https://github.com/srishtis/assignment2-ss1078.git
```

2. Then run the following command to pull the docker image:

```
docker pull ss2809/assignment2-ss1078
```

3. Run the app using the following command:

```
docker run --rm -p 5000:5000 ss2809/assignment2-ss1078
```

### FYI

A simplified version of the app using redis and docker compose can be found [here](https://github.com/srishtis/assignment2-ss1078)

### Demo (for use with docker-compose):

A demo video of how to use the app has been added to the repo [![here](https://img.youtube.com/vi/AiZT15TO7oE/0.jpg)](https://www.youtube.com/watch?v=AiZT15TO7oE)
