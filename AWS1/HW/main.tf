resource "local_file" "file" {
    content  = "Hello, World!"
    filename = "${path.module}/hello${count.index}.txt"
    count = 3
}

resource "local_file" "anotherfile" {
    content  = "Another Hello, World!"
    filename = "${path.module}/anotherHello${each.value}.txt"
    for_each = toset(["one", "two", "three"])
}