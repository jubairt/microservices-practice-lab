# 🧩 Distributed Systems & Microservices Practice

This repository contains my hands-on practice with various **Distributed System Components**, **Microservices Architecture**, and **Service Communication Tools**.  
Each folder demonstrates a specific concept or tool used in modern backend development — from service discovery and load balancing to messaging and API design.

---

## 👨‍💻 Author
**Jubair Abdulla**

---

## 🚀 Overview

This project collection showcases implementations of essential microservices technologies and tools.  
Each demo focuses on one area — helping to understand how distributed systems work together efficiently, reliably, and at scale.

---

## 🧠 Modules Included

### 🧾 `rest_demo`
Basic REST API service built using **FastAPI**, implementing CRUD operations and modular structure.  
Focus: REST fundamentals, routing, and response modeling.

---

### 🔐 `crud_microservice`
A practical microservice performing **CRUD operations** using **FastAPI + SQLAlchemy + SQLite**.  
Includes JWT authentication and structured logging.

---

### ⚙️ `grpc_request_demo`
Exploration of **gRPC** for high-performance, low-latency communication between services.  
Focus: Protocol Buffers, gRPC server & client setup.

---

### 🔄 `kafka_demo`
Integration with **Apache Kafka** for real-time message streaming between producers and consumers.  
Focus: Asynchronous communication and event-driven design.

---

### 🧭 `consul_demo`
Implementation of **HashiCorp Consul** for service discovery and health checks.  
Focus: Dynamic service registration and discovery in microservice environments.

---

### ⚖️ `load_balancing_concul`
Demonstrates **load balancing** using **Consul + Nginx**, ensuring traffic is evenly distributed among instances.

---

### 🪶 `rabitmq_demo`
Showcases **RabbitMQ** for reliable message queuing between microservices.  
Focus: Producer-consumer model and asynchronous task handling.

---

### 🧱 `etcd_demo`
Experiment with **etcd**, a distributed key-value store used for configuration and coordination in microservices.  
Focus: Leader election and service registry.

---

## 📊 Monitoring (Prometheus Integration)

Prometheus is used for **metrics collection and monitoring** across services.  
Each microservice exposes `/metrics` endpoints to allow Prometheus to scrape data such as:

- Request count  
- Latency and error rates  
- Response times  

> This setup can be visualized using **Grafana** for creating rich dashboards.

---

## 🧰 Tools & Technologies Used
- **FastAPI**
- **gRPC**
- **RabbitMQ**
- **Kafka**
- **Consul**
- **etcd**
- **Prometheus**
- **SQLAlchemy**
- **Python 3.10+**

---

## 🧭 Future Plans
- Containerize all services using **Docker**
- Orchestrate using **Kubernetes**
- Add **Grafana dashboards** for visual metrics
- Implement an **API Gateway** for unified routing

---

## 🏁 Conclusion
This repository serves as a complete practical guide for mastering **Microservices Architecture** and **Distributed Systems**.  
It blends multiple technologies to demonstrate how scalable and observable systems are built in real-world environments.
