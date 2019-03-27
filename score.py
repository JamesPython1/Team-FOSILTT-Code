import sys
from Adafruit_IO import MQTTClient
import datetime
from pushbullet import Pushbullet
import os
pb = Pushbullet('')  #This has an access codes in it normally but I have removed it


ADAFRUIT_IO_USERNAME = "" #This has an access codes in it normally but I have removed it
ADAFRUIT_IO_KEY = ""  #This has an access codes in it normally but I have removed it
FEED_ID = 'tt'

sc=[]
dt=None
dd=None
def connected(client):
    print('Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID))
    client.subscribe(FEED_ID)


def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload):
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    if payload == "134":
       print(payload)
       with open("sc.txt", "rb") as pic:
                       file_data = pb.upload_file(pic, "scores_FOSIL.txt")      
                       push = pb.push_file(**file_data)
       del sc[:]
       return
    sc.append(payload)
    f=open('sc.txt', 'w')
    for item in sc:
       f.write("%s\n" % item)
    f.close()
    
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)


client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

client.connect()

client.loop_background()
i=0
while True:
        i=i+1


