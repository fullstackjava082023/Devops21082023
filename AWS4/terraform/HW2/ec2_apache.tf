provider "aws" {
  region = "us-east-1"  
}



# my ec2 instance (compute)
resource "aws_instance" "ec2-instance1" {
    ami           = "ami-0866a3c8686eaeeba" # ubuntu 24.04
    instance_type = "t2.micro" # free tier # 1 vCPU, 1 GiB RAM
    key_name = "my-first-instance-key"
    tags = {
        Name = "Apache2_Terraform"
        description = "webServer with apache"
    }
      provisioner "remote-exec" {
        inline = [ "sudo apt update",
                    "sudo apt install apache2 -y" ]
       
    }
     connection {
            type     = "ssh"
            user = "ubuntu"
            private_key = file("~/.aws/my-first-instance-key.pem")
            host = self.public_ip
        }

    vpc_security_group_ids = ["sg-09aa2f6e34630e81d"]
}