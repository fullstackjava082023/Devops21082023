# optional variable
variable "instance_type" { 
  description = "The type of instance to start"
  default     = "t2.micro"
  type = string
}

# required variable
variable "instance_name" {
  description = "The name of the instance"
  type = string
}