# mqtt-to-metrics
Tiny server for mqtt metrics exposed in  prometheus format.
_no error handling at this time_ 

## mqtt-to-scrap.py ##
Relies on  
* [Python 3](https://docs.python.org/3.3/index.html)
* [cherrypy](https://cherrypy.org/) for webserver
* [paho mqtt](https://pypi.org/project/paho-mqtt/) for mqtt client


```
usage: mqtt-to-scrap.py [-h]  [--broker-host BROKER_HOST] [--broker-port BROKER_PORT] [--broker-topic BROKER_TOPIC] [--broker-qos BROKER_QOS]

optional arguments:
  -h, --help            show help message and exit
  --broker-host         Address of broker
  --broker-port         Port of broker
  --broker-topic        Topic to subscribe to
  --broker-qos          Broker QOS
``` 

## docker / podman ##
Exposes prometheus endpoint `/metrics` on port `8080`.
```
usage: docker run ... [--broker-host BROKER_HOST] [--broker-port BROKER_PORT] [--broker-topic BROKER_TOPIC] [--broker-qos BROKER_QOS]

```


