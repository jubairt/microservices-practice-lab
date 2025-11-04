from etcd3 import Etcd3Client
import requests

etcd = Etcd3Client(host='localhost', port=2379)
user_url = etcd.get('/services/user-service')[0].decode()
product_url = etcd.get('/services/product-service')[0].decode()

user_data = requests.get(f"{user_url}/users").json()
product_data = requests.get(f"{product_url}/products").json()

print("🧾 Order created:", user_data[0]['name'], "ordered", product_data[0]['name'])
