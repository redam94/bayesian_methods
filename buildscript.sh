#!bin/bash
IMAGE="redam94/bayesian_methods"

docker pull ${IMAGE}:latest || \
  true

docker buildx build \
  --cache-from ${IMAGE}:latest \
  -t ${IMAGE}:latest \
  --platform=linux/arm64/v8,linux/amd64 -f Dockerfile . --push