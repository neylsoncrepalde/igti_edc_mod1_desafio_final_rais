#!/bin/bash
set -e

cd etl/

# Push to AWS ECR
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 127012818163.dkr.ecr.us-east-2.amazonaws.com
docker build -t igti-ney-prod-extract-rais .
docker tag igti-ney-prod-extract-rais:latest 127012818163.dkr.ecr.us-east-2.amazonaws.com/igti-ney-prod-extract-rais:latest
docker push 127012818163.dkr.ecr.us-east-2.amazonaws.com/igti-ney-prod-extract-rais:latest
