# NER as a (Micro)Service

The aim of the project is to provide NER using MITIE for Ukrainian language without the need of installing MITIE.

# Usage

## Docker

Easiest way to run it though the Docker (even on Windows). Once you have Docker installed, do the following:

```
docker run -it -p 8080:8080 chaliy/ner-ms
```

## Hosted

Eventually we will provide hosted entry point for your disposal. Ping me in case of urgency.

## Examples

### Curl

Show info about service
```
curl http://localhost:8080/ner
```

Tokenize with default tokenizer and extract named entities

```
curl -X POST -d "Несе Галя воду, Коромисло гнеться, За нею Іванко, Як барвінок, в’ється." http://localhost:8080/ner/text
```

Extract named entities for already tokenized text

```
curl -X POST -H "Content-Type: application/json; charset=UTF-8" -d '{ "tokens": ["Несе","Галя","воду",",","Коромисло","гнеться" ]}' http://localhost:8080/ner
```

# References

Work is based or adaptation of this projects:
 - https://github.com/unchartedsoftware/mitie-server - Docker image to serve MITIE
 - http://lang.org.ua/models/ - MITIE NER model for UK
 - https://github.com/mit-nlp/MITIE - MITIE itself

# License

MIT
