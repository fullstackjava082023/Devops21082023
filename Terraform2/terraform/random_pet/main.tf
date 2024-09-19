resource "local_file" "name" {
    # content  = "${var.file-content["content1"]} ${var.file-content["content2"]}"
    filename = var.filenames[1]
    content = "My favorite pet is ${random_pet.name.id}  and prefix is ${random_pet.name.prefix}"
}

resource "random_pet" "name" {
    length    = var.length
    separator = var.separator
    prefix = var.prefix
}


