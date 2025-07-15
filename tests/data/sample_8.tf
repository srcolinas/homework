
resource "aws_dynamodb_table" "execution_control" {
  name = "${var.prefix}-execution-control"
  ## homework:replace:on
  # billing_mode = ...
  # read_capacity = ...
  # write_capacity = ...
  billing_mode   = "PROVISIONED"
  read_capacity  = 1000
  write_capacity = 1000
  ## homework:replace:off
  
  hash_key = "ExecutionID"

  attribute {
    name = "ExecutionID"
    type = "S"
  }
  tags = var.tags
}

