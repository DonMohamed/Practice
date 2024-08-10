# main.tf
provider "aws" {
  region = "us-east-1"
  }

resource "aws_instance" "app" {
  count         = 3
  ami           = "ami-06f4fa348c295a6f6"
  instance_type = "t2.micro"
  key_name      = "vockey"

  tags = {
    Name = "Ansible-Docker-Instance"
  }
}

output "instance_ips" {
  value = aws_instance.app[*].public_ip
}