terraform {
  required_providers {
    linode = {
      source  = "linode/linode"
      version = "2.25.0"
    }
  }
}

# Configure the Linode Provider
provider "linode" {
  token = "e03c1a233af2f0126c7e334462e24d489e2c0b82dbc4226f0a6c1af10786a9d6"
}


# Create a Linode Instance
resource "linode_instance" "linodePC" {
  label           = "simple_instance"
  image           = "linode/ubuntu24.04"
  region          = "us-mia"
  type            = "g6-nanode-1"
  authorized_keys = ["ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOwkf/kxZzS2eXP+xXuxfawsjVFFPVEq4dv6h7C+a1jQ default"]
  root_pass       = "this-is-not-a-safe-password"


# to print ip ADDRESS  of the created linode inside the file linode_ip.txt
    # ${linode_instance.linodePC.ip_address}


#   tags       = ["foo"]
#   swap_size  = 256
#   private_ip = true
}

resource "linode_instance" "linodePC2" {
  label           = "simple_instance"
  image           = "linode/ubuntu24.04"
  region          = "us-mia"
  type            = "g6-nanode-1"
  authorized_keys = ["ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOwkf/kxZzS2eXP+xXuxfawsjVFFPVEq4dv6h7C+a1jQ default"]
  root_pass       = "this-is-not-a-safe-password"


# to print ip ADDRESS  of the created linode inside the file linode_ip.txt
    # ${linode_instance.linodePC.ip_address}


#   tags       = ["foo"]
#   swap_size  = 256
#   private_ip = true
}