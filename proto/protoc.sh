#!/bin/sh

set -xe

CLIENT_OUTPUT_DIR=/output/client

protoc --version
protoc -I=/proto/protos analyze.proto\
  --go_out=plugins="grpc:${CLIENT_OUTPUT_DIR}" \

python3 protoc.py

sed -i -e 's/from protos/from ./g' /output/server/protos/analyze_pb2_grpc.py > /dev/null