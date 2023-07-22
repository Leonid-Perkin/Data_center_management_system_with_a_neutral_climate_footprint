import random
import time
import csv
from paho.mqtt import client as mqtt_client

broker = '10.3.141.89'
#port = 1883
#broker = 'localhost'
port = 1883
#DC
topic1 = "python/year"
topic2 = "python/Recycled_heat"
topic3 = "python/Emissions"

client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'rosatom'
password = 'rosatom'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %dn", rc)

    client = mqtt_client.Client("test")
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client,data_DC):
    while True:
        for i in range(len(data_DC)):
            result = client.publish(topic1, data_DC[i][0]) 
            result = client.publish(topic2, data_DC[i][1])
            result = client.publish(topic3, data_DC[i][2])
            time.sleep(1)


def main():
    client = connect_mqtt()
    client.loop_start()
    
    fake_data = []
    with open('test.csv', newline='') as File:  
        data = csv.reader(File)
        for row in data:
            a = ','.join(row)
            b = a.split(',')
            fake_data.append(b)
    publish(client,fake_data)


if __name__ == '__main__':
    main()