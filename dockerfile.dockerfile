FROM python:3.11

WORKDIR /app

COPY python/parent_loop.py /app/tweeter-files/python/
COPY python/tweeter.py /app/tweeter-files/python/
COPY README.md /app/tweeter-files/
COPY LICENCE.txt /app/tweeter-files/

RUN pip install tweepy==4.14.0

CMD [ "python", "/app/tweeter-files/python/parent_loop.py"]