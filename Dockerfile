FROM python:3.5-alpine
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt
CMD ["python", "app.py"]
