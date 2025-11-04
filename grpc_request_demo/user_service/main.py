from concurrent import futures
import grpc
import user_pb2
import user_pb2_grpc

class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        return user_pb2.UserResponse(name="Jubi")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:50051")
    print("✅ User service running on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
