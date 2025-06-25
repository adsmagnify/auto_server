# import datetime
# import requests
# import time

# email = "test"
# counter = 1
# uri = "https://adsmagnify-reporting.onrender.com/check-email"

# while True:
#     date = str(datetime.datetime.now())
#     time1 = date.split(" ")
#     minute = time1[1].split(":")[1]
    
#     if(float(minute) % 12 == 0 and counter == 1) :
#         counter = 0
#         print("Sending Request to server - ",  date)
#         requests.post(uri, json={'email': email}, headers={'Content-Type': 'application/json'})
#         print("Going to sleep now")
#         print(" ")
#         time.sleep(690)

#     elif(float(minute) % 12 != 0):
#         counter = 1
#         # print("elif triggered")
#         # print(" ")

import requests

email = "test"
uri = "https://adsmagnify-reporting.onrender.com/check-email"

print("Sending Request to server")
requests.post(uri, json={'email': email}, headers={'Content-Type': 'application/json'})

