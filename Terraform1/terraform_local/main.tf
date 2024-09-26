resource "local_file" "pet" {
  filename = "pets.txt"
  content = var.content[1]
}

