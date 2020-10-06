import time
import grpc
from src.analyze.presentation.grpc import analyze_pb2
from src.analyze.presentation.grpc import analyze_pb2_grpc
from concurrent import futures


class Server(analyze_pb2_grpc.AnalyzeServicer):
    # 初期化
    def __init__(self):
        pass

    # 受信時の処理
    def Sentiment(self, request, context):
        return analyze_pb2.SentimentResponse(score=1.0)


# サーバーの開始
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
analyze_pb2_grpc.add_AnalyzeServicer_to_server(Server(), server)
server.add_insecure_port('[::]:8001')
server.start()
print('Running...')

# 待機
try:
    while True:
        time.sleep(3600)
except KeyboardInterrupt:
    # サーバーの停止
    server.stop(0)
