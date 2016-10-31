# NER as a (Micro)Service

The aim of the project is to provide NER using MITIE for Ukrainian language without the need of installing MITIE.

# Usage

## Docker

Easiest way to run it though the Docker (even on Windows). Once you have Docker installed, do the following:

```
docker run -it -p 8080:8080 chaliy/ner-ms
```

## Hosted

Eventually we will provide hosted entry point for your disposal. Temporary you can use:

```
http://proto.63fgxzp2pg.eu-central-1.elasticbeanstalk.com/ner/mitie/uk
```

## Examples

### Curl

Show info about service
```
curl http://localhost:8080/ner/mitie/uk
```

Extract named entities for already tokenized text

```
curl -X POST -H "Content-Type: application/json; charset=UTF-8" -d '{ "tokens": ["Несе","Галя","воду",",","Коромисло","гнеться" ]}' http://localhost:8080/ner/mitie/uk
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
