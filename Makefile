.PHONY: all

build:
	docker build --rm=false -f uk.Dockerfile -t chaliy/ner-ms:uk .

run:
	docker run -it -p 8080:8080 chaliy/ner-ms:uk

dev:
	docker run -it -p 8080:8080 -v ./src://app ner sh

mike-dev:
	docker run -it -p 8080:8080 -v //c/Users/mchalyi/Projects/ner-ms/src://app ner sh

mike-run-dev:
	docker run -it -p 8080:8080 -v //c/Users/mchalyi/Projects/ner-ms/src://app ner
