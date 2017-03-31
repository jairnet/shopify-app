import requests
import pickle


with open('pruebafinal.txt','rb') as f:
    data = pickle.load(f)





r = requests.post('http://190.159.249.74:8000/orders/', data=data)
print r.status_code
print r.json()


