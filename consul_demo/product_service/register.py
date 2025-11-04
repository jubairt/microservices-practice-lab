import requests, socket

def register_service(service_name, port):
    consul_url = "http://localhost:8500/v1/agent/service/register"
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    payload = {
        "Name": service_name,
        "Address": ip_address,
        "Port": port,
        "Check": {
            "HTTP": f"http://{ip_address}:{port}/health",
            "Interval": "10s"
        }
    }

    requests.put(consul_url, json=payload)
    print(f"✅ Registered {service_name} at {ip_address}:{port}")
