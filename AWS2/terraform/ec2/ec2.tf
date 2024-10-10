provider "aws" {
  region = "us-east-1"  
}


# my ec2 instance (compute)
resource "aws_instance" "ec2-instance2" {
    ami           = "ami-0c0bfbb8624232a8e"
    instance_type = "t2.micro" # free tier # 1 vCPU, 1 GiB RAM
    key_name = "my-first-instance-key"
    tags = {
        Name = "webServer2"
    }
    provisioner "local-exec" {
        command = "echo my ip is ${self.public_ip} > output.txt"
    }

    vpc_security_group_ids = [aws_security_group.webServer.id]
}

resource "aws_instance" "ec2-instance3" {
    ami           = "ami-0c0bfbb8624232a8e"
    instance_type = "t2.micro" # free tier # 1 vCPU, 1 GiB RAM
    key_name = "my-first-instance-key"
    tags = {
        Name = "webServer3"
    }
    provisioner "remote-exec" {
        inline = [ "echo 'Hello, World' > output.html" ]
       
    }
     connection {
            type     = "ssh"
            user = "ubuntu"
            private_key = file("~/.aws/my-first-instance-key.pem")
            host = self.public_ip
        }

    vpc_security_group_ids = [aws_security_group.webServer.id]
}




# my ec2 instance (compute)
resource "aws_instance" "ec2-instance1" {
    ami           = "ami-0c0bfbb8624232a8e"
    instance_type = "t2.micro" # free tier # 1 vCPU, 1 GiB RAM
    key_name = "my-first-instance-key"
    tags = {
        Name = "webServer"
        description = "webServer with apache"
    }
    user_data = <<-EOF
                #!/bin/bash
                echo "Hello, World" > index.html
                EOF

    vpc_security_group_ids = [aws_security_group.webServer.id]
}

resource "aws_security_group" "webServer" {
    tags = {
        Name = "Allow HTTP and SSH inbound traffic"
        description = "Allow HTTP and SSH inbound traffic"
    }
    name        = "webServer"
    description = "Allow HTTP and SSH inbound traffic"
    # vpc_id      = "vpc-0c0bfbb8624232a8e"

    ingress {
        description = "HTTP"
        from_port   = 80
        to_port     = 80
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    # allow ssh
    ingress {
        description = "SSH"
        from_port   = 22
        to_port     = 22
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

output "IP" {
    value = aws_instance.ec2-instance1.public_ip  
}