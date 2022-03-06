variable "region_id" {
  default = "us-east-2"
}

variable "prefix" {
  default = "igti_ney_df_rais"
}

variable "account" {
  default = 127012818163
}

# Prefix configuration and project common tags
locals {
  prefix = "${var.prefix}-${terraform.workspace}"
  common_tags = {
    Project      = "RAIS"
    ManagedBy    = "Terraform"
    Department   = "IGTI",
    Provider     = "A3DATA",
    Owner        = "Data Engineering"
    BusinessUnit = "Data"
    Billing      = "Infrastructure"
    Environment  = terraform.workspace
    UserEmail    = "neylson.crepalde@a3data.com.br"
  }
}

variable "bucket_names" {
  description = "Create S3 buckets with these names"
  type        = list(string)
  default = [
    "landing-zone",
    "processing-zone",
    "delivery-zone"
  ]
}

variable "database_names" {
  description = "Create databases with these names"
  type        = list(string)
  default = [
    #landing-zone
    "dl_landing_zone",
    "dl_rocessing_zone",
    "dl_delivery_zone"
  ]
}

variable "bucket_paths" {
  description = "Paths to S3 bucket used by the crawler"
  type        = list(string)
  default = [
    "s3://landing-zone",
    "s3://processing-zone",
    "s3://delivery-zone"
  ]
}

variable "bucket_functions" {
  description = "Create S3 bucket for lambda functions"
  default     = "temp-functions-rony"
}