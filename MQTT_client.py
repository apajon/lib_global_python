import paho.mqtt.client as mqtt #import the client

def createClient(clientName,config):
    #create client connected to mqtt broker

    #create new instance
    print(f"MQTT creating new instance named : {str(clientName)}")
    client = mqtt.Client(clientName) 

    #set username and password
    print("MQTT setting  password")
    client.username_pw_set(username=config.get('MQTT','usr'),password=config.get('MQTT','pswd'))

    #connection to broker
    broker_address=config.get('MQTT','broker_address')
    print(f"MQTT connecting to broker : {broker_address}")
    client.connect(broker_address) #connect to broker

    return client