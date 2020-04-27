FROM python:3.6
RUN mkdir -p /usr/src/app
COPY ./src/ /usr/src/app/
COPY docker-entrypoint.sh /

WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/docker-entrypoint.sh"]
