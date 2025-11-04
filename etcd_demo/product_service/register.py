from etcd3 import Etcd3Client
import socket

def register_service(service_name, port):
    etcd = Etcd3Client(host='localhost', port=2379)
    ip = socket.gethostbyname(socket.gethostname())
    key = f"/services/{service_name}"
    value = f"http://{ip}:{port}"
    etcd.put(key, value)
    print(f"✅ Registered {service_name} at {value}")
