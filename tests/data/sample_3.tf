terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  ## homework:replace:on
  # profile = ...
  profile = "ExpertiseBuilding"
  ## homework:replace:off
  region = "us-east-1"

  default_tags {
    tags = {
      Topic = "terraform"
      ## homework:replace:on
      # Owner = ...
      Owner = "srcolinas"
      ## homework:replace:off
    }
  }
}

resource "aws_s3_bucket" "bucket" {
  ## homework:replace:on
  # bucket = ...
  bucket = "srcolinas-0b030605-a7d2-41b3-848f-0f4b8298ee12"
  ## homework:replace:off
}
