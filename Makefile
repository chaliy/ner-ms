.PHONY: all

build:
	docker build -t ner .

run:
	docker run -it -p 8080:8080 ner

dev:
	docker run -it -p 8080:8080 -v ./src://app ner bash

mike-dev:
	docker run -it -p 8080:8080 -v //c/Users/mchalyi/Projects/ner-ms/src://app ner bash
