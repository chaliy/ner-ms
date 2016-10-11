FROM centos:centos7

RUN yum -y install epel-release
RUN yum -y groupinstall 'Development Tools'
RUN yum -y install git make wget tar bzip2
RUN yum -y install install -y python python-devel python-distribute python-pip

RUN cd /; git clone https://github.com/mit-nlp/MITIE.git
RUN cd /MITIE; make

#RUN cd /MITIE; make MITIE-models
RUN wget http://lang.org.ua/static/downloads/ner_models/uk_model.dat.bz2 \
    && bzip2 -d uk_model.dat.bz2

ADD src /app
RUN cd /app; pip install -r requirements.txt

EXPOSE 8080
ENV PORT "8080"
ENV HOST "0.0.0.0"
CMD ["/app/server.py"]
