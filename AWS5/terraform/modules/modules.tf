# module "ec2" {
#   source = "../ec2"
#   instance_name = "myterraformmoduleinstance"
#   # optional variable
#   instance_type = "t3.micro"
# }


# module "ssh_security_group" {
#   source  = "terraform-aws-modules/security-group/aws//modules/ssh"
#   version = "5.2.0"

#   name = "allowsshtf"
#   vpc_id = "vpc-095cd15c99baabd30"  
  
# }


module "my-vpc" {
    source = "terraform-aws-modules/vpc/aws"
    version = "5.14.0"
    name = "my-tf-module-vpc"
}


module "vpc2" {
  source = "terraform-aws-modules/vpc/aws"
  version = "5.14.0"
  name = "vpc-tf-with-variables"
  cidr = "10.10.0.0/16"
  azs             = ["us-east-1a", "us-east-1b"]
  private_subnets = ["10.10.1.0/24", "10.10.2.0/24", "10.10.1.0/24"]
  public_subnets  = ["10.10.101.0/24", "10.10.102.0/24"]
  enable_nat_gateway = true
  single_nat_gateway = true
}

