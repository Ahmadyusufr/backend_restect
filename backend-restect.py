import paho.mqtt.client as mqttClient
import time
import requests
import pymongo
# import RPi.GPIO as GPIO
from time import sleep
from flask import Flask
# from signal import signal, SIGTERM, SIGHUP, pause
# from rpi_lcd import LCD
from datetime import datetime

app = Flask(__name__)

Connected = False #global variable for the state of the connection
  
broker_address= "industrial.api.ubidots.com"
port = 1883
user = "BBFF-Hek4803AKZmWhVxuyvOx1ygKnYetJn"
password = "BBFF-Hek4803AKZmWhVxuyvOx1ygKnYetJn"

def on_connect(client, userdata, flags, rc):
  
    if rc == 0:
  
        print("Connected to broker")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
  
    else:
  
        print("Connection failed")
  
def on_message(client, userdata, message):
    print ("Message received: "  + message.payload)
  
Connected = False   #global variable for the state of the connection
  
client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
  
client.connect(broker_address, port=port)          #connect to broker
  
client.loop_start()        #start the loop
  
while Connected != True:    #Wait for connection
    time.sleep(0.1)
  
client.subscribe("/v1.6/devices/restect/switch/lv")
  

# TOKEN = "BBFF-Hek4803AKZmWhVxuyvOx1ygKnYetJn"
# DEVICE_LABEL = "ReSTect" 
# VARIABLE_LABEL_1 = "gas"
# VARIABLE_LABEL_2 = "flame"
# VARIABLE_LABEL_3 = "servo"
# VARIABLE_LABEL_4 = "buzzer"

# GPIO.setmode(GPIO.BCM)  
# GPIO.setwarnings(False)  

# GPIO.setup(26, GPIO.IN)  #gas
# GPIO.setup(21, GPIO.IN)  #flame
# GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP) #button
# GPIO.setup(23, GPIO.OUT) #buzzer
# GPIO.setup(17, GPIO.OUT) #servo
 
# pwm=GPIO.PWM(17, 50)
# pwm.start(0)
# lcd = LCD()

# def build_payload(variable_1, variable_2, variable_3, variable_4):
#     gas = GPIO.input(26)
#     flame = GPIO.input(21)
#     button = GPIO.input(16)
#     buzzer = GPIO.output(23)
#     servo = GPIO.output(17)
#    
# def SetAngle(angle):
#         duty = angle / 18 + 2
#         GPIO.output(17, True)
#         pwm.ChangeDutyCycle(duty)
#         sleep(1)
#         GPIO.output(17, False)
#         pwm.ChangeDutyCycle(0)
        
# def safe_exit(signum, frame):
#     exit(1)

# while True:
#     gas = GPIO.input(26)
#     button = GPIO.input(16)
#     flame = GPIO.input(21)
#     #print(button)
#     if gas == 0:                 #When output from LPG sensor is LOW  
#         print("Gas Aman",gas)
#         time.sleep(0.5)
#         try:
#             lcd.text("    Gas Aman", 1)
#             lcd.text(    str(datetime.now().time()), 2)
#         except KeyboardInterrupt:
#             pass
#         if button == 0:
#             GPIO.output(23, GPIO.LOW)
#     elif gas == 1:               #When output from LPG sensor is HIGH  
#     #print("Intruder detected",i)
#         SetAngle(90)
#         time.sleep(0.3)
#         print("Gas Bocor",gas)
#         try:
#             lcd.text("Gas Bocor", 1)
#             lcd.text(str(datetime.now().time()), 2)
#         except KeyboardInterrupt:
#             pass
#         if button == 1 :
#             GPIO.output(23, GPIO.HIGH)
#         else :
#             GPIO.output(23, GPIO.LOW)
#     if flame == 0:
#        print("api nyala")
#     elif flame == 1:
#        print("api mati")
#     sleep(1)

#     payload = {variable_1:gas, variable_2:flame, variable_3:buzzer, variable_4:servo}
    
#     print(payload)
#     return payload

# def post_request(payload):
#     # Creates the headers for the HTTP requests
#     url = "http://industrial.api.ubidots.com"
#     url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
#     headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

#     # Makes the HTTP requests
#     status = 400
#     attempts = 0
#     while status >= 400 and attempts <= 5:
#         req = requests.post(url=url, headers=headers, json=payload)
#         status = req.status_code
#         attempts += 1
#         time.sleep(1)

#     # Processes results
#     print(req.status_code, req.json())
#     if status >= 400:
#         print("[ERROR] Could not send data after 5 attempts, please check \
#             your token credentials and internet connection")
#         return False

#     print("[INFO] request made properly, your device is updated")
#     return True

# def switch_regulator():

# def main():
#     payload = build_payload(
#         VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3, VARIABLE_LABEL_4)

#     print("[INFO] Attemping to send data")
#     post_request(payload)
#     print("[INFO] finished")


# if __name__ == '__main__':
#     while (True):
#         main()
#         time.sleep(1)