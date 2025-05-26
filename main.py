import datetime
import requests
import time

email = "test"
counter = 1
uri = "https://adsmagnify-reporting.onrender.com/check-email"

while True:
    date = str(datetime.datetime.now())
    time = date.split(" ")
    minute = time[1].split(":")[1]
    
    if(float(minute) % 10 == 0 and counter == 1) :
        counter = 0
        print("hi")
        requests.post(uri, json={'email': email}, headers={'Content-Type': 'application/json'})
        time.sleep(480)

    elif(float(minute) % 10 != 0):
        counter = 1
    
