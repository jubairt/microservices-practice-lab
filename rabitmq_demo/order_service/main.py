import pika, json

url = "amqps://tdipdrdy:p1qHp0Ac00d2ZuGtsGDabhItNyYtqDTF@beaver.rmq.cloudamqp.com/tdipdrdy"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='orders')

def callback(ch, method, properties, body):
    order = json.loads(body)
    print("📦 Received order:", order)

channel.basic_consume(queue='orders', on_message_callback=callback, auto_ack=True)
print("👂 Waiting for orders... Press Ctrl+C to exit")
channel.start_consuming()
