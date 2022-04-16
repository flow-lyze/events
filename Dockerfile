FROM python:3.8.2-alpine

COPY . .
WORKDIR .

# required step for installing uvloop package on Alpine Image
RUN apk add build-base

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT ["uvicorn", "app.main:server", "--reload"]
