FROM python:3.8.2-alpine

COPY . .
WORKDIR .

EXPOSE 8000

# required step for installing uvloop package on Alpine Image
RUN apk add build-base

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

# Running Unit Tests
RUN pytest app/tests

ENTRYPOINT ["python3", "app/main.py"]
