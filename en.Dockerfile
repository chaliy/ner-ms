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
    bzip2 \
	&& cd / \
	&& curl -fSL https://github.com/mit-nlp/MITIE/releases/download/v0.4/MITIE-models-v0.2.tar.bz2 -o MITIE-models-v0.2.tar.bz2 \
	&& tar -xjf MITIE-models-v0.2.tar.bz2 \
  && mv MITIE-models/english/ner_model.dat en_model.dat \
	&& rm MITIE-models-v0.2.tar.bz2 \
	&& rm -rf MITIE-models \
	&& apk del .fetch-deps

ENV MITIE_MODEL /en_model.dat
ENV MITIE_MODEL_LANG en

ADD src /app
RUN set -ex \
  && cd /app \
  && pip3 install -r requirements.txt --no-cache-dir

EXPOSE 8080
CMD ["python", "/app/server.py"]
