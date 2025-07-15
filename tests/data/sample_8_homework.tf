
resource "aws_dynamodb_table" "execution_control" {
  name = "${var.prefix}-execution-control"
  ## homework:start
  billing_mode = ...
  read_capacity = ...
  write_capacity = ...
  ## homework:end

  hash_key = "ExecutionID"

  attribute {
    name = "ExecutionID"
    type = "S"
  }
  tags = var.tags
}

