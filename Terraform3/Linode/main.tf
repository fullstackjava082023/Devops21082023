terraform {
  required_providers {
    linode = {
      source  = "linode/linode"
      version = "2.25.0"
    }
  }
}

provider "linode" {
  token = var.linode_token
}


# this resource will be created first
resource "linode_instance" "linodePC" {
  label           = "linodeWithTerraform"
  image           = "linode/ubuntu24.04"
  region          = "us-central"
  type            = "g6-nanode-1" # 1GB RAM, 1 CPU, 25GB Storage
  authorized_keys = [var.ssh_key]
  root_pass       = var.root_pass
  tags            = ["terraform"]

}

# this resource will be created after the linode_instance #2
resource "linode_volume" "additional_volume" {
  label     = "additional_volume"
  size      = 10 # 10GB
  region    = linode_instance.linodePC.region
  linode_id = linode_instance.linodePC.id
}


# this resource will be created after the linode_volume #3
resource "local_file" "linode_ip" {
  filename   = "linode_ip.txt"
  content    = "IP Address of the new Linode is : ${linode_instance.linodePC.ip_address}"
  depends_on = [linode_volume.additional_volume]

}


output "instance_ip" {
  value = "linode ip is ${linode_instance.linodePC.ip_address}"
}

output "volume_id" {
  value = linode_volume.additional_volume.id
}