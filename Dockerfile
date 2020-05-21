FROM centos
RUN yum install -y python3 \
    && pip3 install --user paho-mqtt cherrypy
COPY ./mqtt-to-scrap.py /
COPY ./entrypoint.sh    /
EXPOSE 8080
ENTRYPOINT ["/entrypoint.sh"]

