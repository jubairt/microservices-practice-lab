import pika, json

url = "create instance from cloudamqp and paste the id here"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='orders')

order = {"user": "Jubi", "product": "Laptop"}
channel.basic_publish(exchange='', routing_key='orders', body=json.dumps(order))
print("✅ Sent order:", order)

connection.close()
