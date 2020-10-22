import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':40, 'duration':950, 'nr_employed':5100, 'loan':0,})

print(r.json())