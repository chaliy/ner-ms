# NER as a (Micro)Service

The aim of the project is to provide NER using MITIE for Ukrainian language without the need of installing MITIE.

# Usage

## Docker

Easiest way to run it though the Docker (even on Windows). Once you have Docker installed, do the following:

```
git clone git@github.com:chaliy/ner-ms.git
cd ner-ms
docker build -t ner .
docker run -it -p 8080:8080 ner
# Open http://localhost:8080/ner
```

## As is

You can also run app as is on your machine, however this will require all dependencies to be installed. Check Dockerfile for working script.

## Hosted

Eventually we will provide hosted entry point for your disposal. Ping me in case of urgency.

# References

Work is based or adaptation of this projects:
 - https://github.com/unchartedsoftware/mitie-server - Docker image to serve MITIE
 - http://lang.org.ua/models/ - MITIE NER model for UK
 - https://github.com/mit-nlp/MITIE - MITIE itself

# License

MIT
