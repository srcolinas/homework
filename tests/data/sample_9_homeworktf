variable "vpc_cidr_block" {
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
}
variable "availability_zone" {
  description = "Availability zone to deploy the subnet"
  default     = "us-east-1a"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t3.medium"
}


variable "vpc_id" {
  description = "vpc id for the ec2 instance"
  ## homework:replace:on
  # default = ...  
  default     = "vpc-0998974106cb67c74"
  ## homework:replace:off
}


variable "subnet_id" {
  description = "subnet id for the ec2 instance"
  ## homework:replace:on
  # default = ...  
  default     = "subnet-00592906cfd6d9847"
  ## homework:replace:off
}

variable "region" {
  description = "region"
  default     = "us-east-1"
  type        = string
}


variable "volume_size" {
  description = "Root volume size for EC2 instance"
}

variable "expose_apps" {
  description = "Ports to expose on EC2 instance"
  type        = map(number)
}

variable "public_ip_cidr" {
  description = "The IPs in which should have access to connect to the instance"
  default = [
    "0.0.0.0/0",
  ]
}

variable "tags" {
  type = map(any)
  default = {
    environment = "llm_labs"
    project     = "mlt-monitoring-lab2-llmops"
    ManagedBy   = "Terraform"
    ## homework:replace:on
    # created_at  = ""
    created_at  = "2024-11-19"
    ## homework:replace:off    
  }
  description = "The tag for all resources for the llm monitoring lab"
}

variable "prefix" {
  type        = string
  default     = "mlt-monitoring-lab2-llmops"
  description = "The prefix for all resource names"
}
