import random
import time
import csv
from paho.mqtt import client as mqtt_client

broker = '10.3.141.89'
#port = 1883
#broker = 'localhost'
port = 1883
#DC
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
#HU
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

    client = mqtt_client.Client("Python3")
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client,data_DC,data_HU):
    while True:
        for i in range(len(data_DC)):
            # DC
            result = client.publish(topic1, data_DC[i][0]) #DC_Voltage1
            result = client.publish(topic2, data_DC[i][1]) #DC_Voltage2
            result = client.publish(topic3, data_DC[i][2]) #DC_Voltage3
            result = client.publish(topic4, data_DC[i][3]) #DC_Humiditly1
            result = client.publish(topic5, data_DC[i][4]) #DC_Rms1
            result = client.publish(topic6, data_DC[i][5]) #DC_Rms2
            result = client.publish(topic7, data_DC[i][6]) #DC_Rms3
            result = client.publish(topic8, data_DC[i][7]) #DC_Active_power1
            result = client.publish(topic9, data_DC[i][8]) #DC_Active_power2
            result = client.publish(topic10, data_DC[i][9]) #DC_Active_power3
            #HU
            result = client.publish(topic11, data_HU[i][0]) #HU_Pressure1
            result = client.publish(topic12, data_HU[i][1]) #HU_Pressure2
            result = client.publish(topic13, data_HU[i][2]) #HU_Temperature1
            result = client.publish(topic14, data_HU[i][3]) #HU_Temperature2
            result = client.publish(topic15, data_HU[i][2]) #HU_Termal_energy
            result = client.publish(topic16, data_HU[i][3]) #HU_HU_Water
            time.sleep(3)


def main():
    client = connect_mqtt()
    client.loop_start()
    
    fake_data_DC = []
    fake_data_HU = []
    with open('DC.csv', newline='') as File:  
        data = csv.reader(File)
        for row in data:
            a = ','.join(row)
            b = a.split(',')
            fake_data_DC.append(b)
    with open('termal.csv', newline='') as File:  
        data = csv.reader(File)
        for row in data:
            a = ','.join(row)
            b = a.split(',')
            fake_data_HU.append(b)
    #print(fake_data_HU)
    publish(client,fake_data_DC,fake_data_HU)


if __name__ == '__main__':
    main()