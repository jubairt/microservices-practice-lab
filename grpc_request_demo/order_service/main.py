import grpc
import user_pb2, user_pb2_grpc
import product_pb2, product_pb2_grpc

def get_user():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        response = stub.GetUser(user_pb2.UserEmpty())
        return response.name

def get_product():
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = product_pb2_grpc.ProductServiceStub(channel)
        response = stub.GetProduct(product_pb2.ProductEmpty())
        return response.name

if __name__ == "__main__":
    user = get_user()
    product = get_product()
    print(f"🎉 Order created: {user} ordered a {product}")
