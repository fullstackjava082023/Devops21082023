resource "linode_volume" "data_volume" {
  size   = 50 # Size in GB
  linode_id = "sdf35437"
}