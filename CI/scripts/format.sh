#!/bin/bash
set -e

#### Terraform Format AWS #####

./CI/scripts/pre_terraform.sh

cd infrastructure/aws/
terraform fmt
cd ../../

######################################