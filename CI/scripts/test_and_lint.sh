#!/bin/bash
set -e


### Check terraform format

cd infrastructure/aws/
terraform fmt -check
cd ../../

#####################