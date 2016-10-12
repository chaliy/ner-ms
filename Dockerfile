FROM python:3

RUN cd /; git clone https://github.com/mit-nlp/MITIE.git
RUN cd /MITIE; make

# #RUN cd /MITIE; make MITIE-models
RUN wget http://lang.org.ua/static/downloads/ner_models/uk_model.dat.bz2 \
    && bzip2 -d uk_model.dat.bz2

ADD src /app
RUN cd /app; pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "/app/server.py"]
