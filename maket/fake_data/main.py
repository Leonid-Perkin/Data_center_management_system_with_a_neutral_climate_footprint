import random
import time
import csv
from paho.mqtt import client as mqtt_client

broker = '10.3.141.89'
port = 1883
topic1 = "python/DC_Voltage1"
topic2 = "python/DC_Voltage2"
topic3 = "python/DC_Voltage3"
topic4 = "python/DC_Humiditly1"
topic5 = "python/DC_Rms1"
topic6 = "python/DC_Rms2"
topic7 = "python/DC_Rms3"
topic8 = "python/DC_Active_power1"
topic9 = "python/DC_Active_power2"
topic10 = "python/DC_Active_power3"

topic11 = "python/HU_Pressure1"
topic12 = "python/HU_Pressure2"
topic13 = "python/HU_Temperature1"
topic14 = "python/HU_Temperature2"
topic15 = "python/HU_Termal_energy"
topic16 = "python/HU_Water"

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
        for i in range(len(data)):
            result = client.publish(topic1, data[i][0])
            result = client.publish(topic2, data[i][1])
            result = client.publish(topic3, data[i][2])
            result = client.publish(topic4, data[i][3])
            result = client.publish(topic5, data[i][4])
            result = client.publish(topic6, data[i][5])
            result = client.publish(topic7, data[i][6])
            result = client.publish(topic8, data[i][7])
            result = client.publish(topic9, data[i][8])
            result = client.publish(topic10, data[i][9])
            time.sleep(3)


def main():
    client = connect_mqtt()
    client.loop_start()
    
    fake_data = []
    with open('DC.csv', newline='') as File:  
        data = csv.reader(File)
        for row in data:
            a = ','.join(row)
            b = a.split(',')
            fake_data.append(b)
    #print(len(fake_data[0]))
    publish(client,fake_data)


if __name__ == '__main__':
    main()