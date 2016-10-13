FROM python:3-alpine

RUN set -ex \
	&& apk add --no-cache --virtual .build-deps  \
    alpine-sdk \
	&& cd / \
	&& git clone https://github.com/mit-nlp/MITIE.git \
	&& cd /MITIE \
	&& make \
	&& apk del .build-deps \
	&& apk add --no-cache libstdc++

RUN set -ex \
	&& apk add --no-cache --virtual .fetch-deps  \
    curl \
    bzip2 \
	&& cd / \
	&& curl -fSL http://lang.org.ua/static/downloads/ner_models/uk_model.dat.bz2 -o uk_model.dat.bz2 \
	&& bzip2 -d uk_model.dat.bz2 \
	&& apk del .fetch-deps

ADD src /app
RUN set -ex \
  && cd /app \
  && pip3 install -r requirements.txt --no-cache-dir

EXPOSE 8080
CMD ["python", "/app/server.py"]
