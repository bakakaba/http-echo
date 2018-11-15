FROM alpine

RUN apk add --no-cache python3
COPY echoserver /srv/echoserver

EXPOSE 8000
CMD ["python3", "/srv/echoserver"]
