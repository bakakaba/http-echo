FROM python:3-alpine

COPY echoserver /srv/echoserver

EXPOSE 8000
ENTRYPOINT ["python3", "-u", "/srv/echoserver"]
