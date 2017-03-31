import requests
import pickle


with open('pruebafinal.txt','rb') as f:
    data = pickle.load(f)





r = requests.post('https://shopify-5.herokuapp.com/orders/', data=data)
print r.status_code
print r.json()


