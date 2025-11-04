import requests, socket

def register_service(service_name, port):
    consul_url = "http://localhost:8500/v1/agent/service/register"
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    # 👇 Add unique service ID
    service_id = f"{service_name}-{port}"

    payload = {
        "ID": service_id,               # unique identifier
        "Name": service_name,           # same name (for grouping)
        "Address": ip_address,
        "Port": port,
        "Check": {
            "HTTP": f"http://{ip_address}:{port}/health",
            "Interval": "10s"
        }
    }

    requests.put(consul_url, json=payload)
    print(f"✅ Registered {service_id} at {ip_address}:{port}")
