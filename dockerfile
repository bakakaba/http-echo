FROM alpine

RUN apk add --no-cache python3
COPY echoserver /srv/

EXPOSE 8000
CMD ["python3", "/srv/echoserver"]
