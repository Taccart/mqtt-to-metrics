import paho.mqtt.subscribe as subscribe
import re
import struct
import cherrypy
import threading
import argparse


class PARMS:
    pass

parms=PARMS()
parser = argparse.ArgumentParser()
parser.add_argument('--broker-host', help='Address of  broker', default="127.0.0.1")
parser.add_argument('--broker-port', type=int, help='Port of broker', default=1883)
parser.add_argument('--broker-topic', help='Topic to subscribe to',default="#")
parser.add_argument('--broker-qos',  type=int, help='Broker QOS',default=0)




mRE = re.compile('^.?metrics/(\w+)/(\w+)/(\w+)/(\w+)/(\w+)$')
vRE = re.compile ('(\d+)')

metrics = {}
nl='\n'

def on_message_print(client, userdata, message):
    m=mRE.match(message.topic)
    v=vRE.match(message.payload.decode("utf-8") )
    if (not (( m is  None) or (v is None)) ):
        K="%s{%s=\"%s\", %s=\"%s\"} " % ( m.group(5), m.group(1),m.group(2),m.group(3),m.group(4),)
        V=float(v.group(0)) 
        print("store ",K,V)
        metrics[K]=V
    else:
        print ("discard ", message.topic)

def subscr():
    print("Start mqtt subscribe to topic ", parms.broker_topic, parms.broker_host, parms.broker_port)
    subscribe.callback ( callback=on_message_print, topics=parms.broker_topic, hostname=parms.broker_host, port=parms.broker_port, qos=parms.broker_qos )

class Webserver(object):
    @cherrypy.expose
    def metrics(self):
        return (nl.join("{!s} {!r}".format(key,val) for (key,val) in metrics.items()))

def startsvr():
    print("Start webserver.")
    cherrypy.quickstart(Webserver())

if __name__ == '__main__':

    args = parser.parse_args(namespace=parms)
    threading.Thread(target=startsvr).start()
    threading.Thread(target=subscr).start()
    




