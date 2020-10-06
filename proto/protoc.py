from grpc.tools import protoc
protoc.main(
    (
        '',
        '-I.',
        '--python_out=/output/server',
        '--grpc_python_out=/output/server',
        'protos/analyze.proto',
    )
)