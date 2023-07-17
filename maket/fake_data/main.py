import random
import time
import csv
from paho.mqtt import client as mqtt_client

broker = '10.3.141.89'
port = 1883
topic1 = "python/Voltage1"
topic2 = "python/Voltage2"
topic3 = "python/Voltage3"
topic4 = "python/Humiditly1"
topic5 = "python/Rms1"
topic6 = "python/Rms2"
topic7 = "python/Rms3"
topic8 = "python/Active_power1"
topic9 = "python/Active_power2"
topic10 = "python/Active_power3"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'rosatom'
password = 'rosatom'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %dn", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client,data):
    while True:
        for i in data:
            result = client.publish(topic1, i[0])
            result = client.publish(topic2, i[1])
            result = client.publish(topic3, i[2])
            result = client.publish(topic4, i[3])
            result = client.publish(topic5, i[4])
            result = client.publish(topic6, i[5])
            result = client.publish(topic7, i[6])
            result = client.publish(topic8, i[7])
            result = client.publish(topic9, i[8])
            #result = client.publish(topic10, i[9]+'%')
            time.sleep(3)


def main():
    client = connect_mqtt()
    client.loop_start()
    
    fake_data = []
    with open('csvFile.csv', newline='') as File:  
        data = csv.reader(File)
        for row in data:
            a = ','.join(row)
            b = a.split(',')
            fake_data.append(b)
    publish(client,fake_data)


if __name__ == '__main__':
    main()
