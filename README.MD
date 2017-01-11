# NER as a (Micro)Service

The aim of the project is to provide NER using MITIE for Ukrainian language without the need of installing MITIE.

[![CircleCI](https://circleci.com/gh/chaliy/ner-ms.svg?style=svg)](https://circleci.com/gh/chaliy/ner-ms)

## Usage

### Docker

Easiest way to run it though the Docker (even on Windows). Once you have Docker installed, do the following:

```
docker run -it -p 8080:8080 chaliy/ner-ms
```

#### Image Variants

- chaliy/ner-ms:uk Ukrainian NER using Lang-UK model
- chaliy/ner-ms:en English NER using default MITIE model
- chaliy/ner-ms:ru Russian NER using Lang-UK model

## Examples

### Curl

Show info about service
```
curl http://localhost:8080/
```

Extract named entities for already tokenized text

```
curl -X POST -H "Content-Type: application/json; charset=UTF-8" -d '{ "tokens": ["Несе","Галя","воду",",","Коромисло","гнеться" ]}' http://localhost:8080/
```

### Postman

You can get Postman collection from https://www.getpostman.com/collections/c6db7bb555fc76ab57f5

# References

Work is based or adaptation of this projects:
 - https://github.com/unchartedsoftware/mitie-server - Docker image to serve MITIE
 - http://lang.org.ua/models/ - MITIE NER model for UK
 - https://github.com/mit-nlp/MITIE - MITIE itself

# License

MIT
