resource "local_file" "pets" {
    for_each = toset(["cat.txt", "mouse.txt" ])
    filename = each.value
    content = "stam content ${each.key} ${each.value}"
}

resource "local_file" "names" {
    count = 3
    filename = "name${count.index}.txt"
    content = "stam content"
}