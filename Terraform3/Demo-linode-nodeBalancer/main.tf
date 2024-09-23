terraform {
  required_providers {
    linode = {
      source  = "linode/linode"
      version = "2.25.0"
    }
  }
}

# this resource will be created first
resource "linode_instance" "web1_node" {
  label           = "web1_node"
  image           = "linode/ubuntu24.04"
  region          = "us-central"
  type            = "g6-nanode-1" # 1GB RAM, 1 CPU, 25GB Storage
  authorized_keys = [var.ssh_key]
  root_pass       = var.root_pass
  tags            = ["terraform"]
  private_ip = true

}

# this resource will be created first
resource "linode_instance" "web2_node" {
  label           = "web2_node"
  image           = "linode/ubuntu24.04"
  region          = "us-central"
  type            = "g6-nanode-1" # 1GB RAM, 1 CPU, 25GB Storage
  authorized_keys = [var.ssh_key]
  root_pass       = var.root_pass
  tags            = ["terraform"]
  private_ip = true
}


provider "linode" {
  token = var.linode_token
}

resource "linode_nodebalancer" "lb" {
  region = "us-central"  
}

resource "linode_nodebalancer_config" "lb_config" {
    nodebalancer_id = linode_nodebalancer.lb.id
    port = 80
    protocol = "http"
}

resource "linode_nodebalancer_node" "web1_node" {
    nodebalancer_id = linode_nodebalancer.lb.id
    config_id = linode_nodebalancer_config.lb_config.id
    address = "${linode_instance.web1_node.private_ip_address}:80"
    label = "web1"
}

resource "linode_nodebalancer_node" "web2_node" {
    nodebalancer_id = linode_nodebalancer.lb.id
    config_id = linode_nodebalancer_config.lb_config.id
    address = "${linode_instance.web2_node.private_ip_address}:80"
    label = "web2"
}


# output "web1_ip" {
#   value = {
#     private_ip = linode_instance.web1_node.private_ip_address
#     public_ip = linode_instance.web1_node.ip_address
#   }
# }

# output "web2_ip" {
#   value = {
#     private_ip = linode_instance.web2_node.private_ip_address
#     public_ip = linode_instance.web2_node.ip_address
#   }
# }

# output "nodebalancer_ip" {
#   value = linode_nodebalancer.lb.ipv4
# }
