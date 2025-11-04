from concurrent import futures
import grpc
import product_pb2
import product_pb2_grpc

class ProductService(product_pb2_grpc.ProductServiceServicer):
    def GetProduct(self, request, context):
        return product_pb2.ProductResponse(name="Laptop")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    product_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
    server.add_insecure_port("[::]:50052")
    print("✅ Product service running on port 50052")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
