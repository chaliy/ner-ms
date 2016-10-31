FROM python:3-alpine

MAINTAINER Mike Chaliy

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
	&& cd / \
	&& curl -fSL http://lang.org.ua/static/downloads/ner_models/ru_model.dat.bz2 -o ru_model.dat.bz2 \
	&& bzip2 -d ru_model.dat.bz2 \
	&& apk del .fetch-deps

ENV MITIE_MODEL /ru_model.dat
ENV MITIE_MODEL_LANG ru

ADD src /app
RUN set -ex \
  && cd /app \
  && pip3 install -r requirements.txt --no-cache-dir

EXPOSE 8080
CMD ["python", "/app/server.py"]
