variable "arja" {
  default = "We love pets!"
}

variable "filenames" {
  default = ["pets.txt", "dogs.txt", "cats.txt"]
  type = list
}

variable "file-content" {
    default = {
        content1 = "We love pets!!"
        content2 = "We love dogs!"
    }
    type = map
    description = "values of the file"
}

variable "bella" {
  default = {
    name = "bella"
    age = 3
  }
}

variable "filename" {
  default = "pets.txt"
}

variable "length" {
  default = 3  
  type = number
}

variable "separator" {
  default = "."
  type = string
}

variable "prefix" {
  default = "Mr"
}