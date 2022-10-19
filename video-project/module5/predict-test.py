#!/usr/bin/env python
# coding: utf-8

import requests
# host = 'churn-serving-env.eba-ne2dgm8h.ap-south-1.elasticbeanstalk.com'
host = 'localhost:9696'
url = f'http://{host}/predict'
customerid = '0111-klbqg'

customer = {
    "gender": "male",
    "seniorcitizen": 1,
    "partner": "yes",
    "dependents": "yes",
    "tenure": 1,
    "phoneservice": "yes",
    "multiplelines": "no",
    "internetservice": "fiber_optic",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "yes",
    "streamingmovies": "yes",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "mailed_check",
    "monthlycharges": 93.95,
    "totalcharges": 2861.45,
 }

response = requests.post(url, json=customer).json()
print(response)

if response['churn'] == True:
    print('Sending promo email to %s' % (customerid))
else:
    print('Not sending promo email to %s' % (customerid))
