import requests

host = 'localhost:9696'
url = f'http://{host}/predict'

client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}

response = requests.post(url, json=client).json()
y_pred = response['credit_card_getting_prob']
print(f'The client will get a credit card with probability: {y_pred}')