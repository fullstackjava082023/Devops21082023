provider "aws" {
  region = "us-east-1"  
}


resource "aws_s3_bucket" "example" {
  bucket = "jonsnowbucket"
}

resource "aws_s3_object" "object1" {
  key = "pets.txt"
  content = "we love pets!"
  bucket = aws_s3_bucket.example.id
}

data "aws_s3_bucket" "arjabucket" {
  bucket = "arjastarkbucket"
}


resource "aws_s3_object" "object2" {
  key = "pets.txt"
  content = "we love pets!"
  bucket = data.aws_s3_bucket.arjabucket.id
}



resource "aws_s3_object" "object3" {
  key = "aws.py"
  source = "../../main.py"
  bucket = data.aws_s3_bucket.arjabucket.id
}


resource "aws_s3_bucket_public_access_block" "my_bucket_public_access" {
  bucket = aws_s3_bucket.example.id
  block_public_acls       = false
  ignore_public_acls      = false
  block_public_policy     = false
  restrict_public_buckets = false
}


resource "aws_s3_bucket_policy" "public_bucket_policy" {
  bucket = aws_s3_bucket.example.id
  policy = jsonencode({
                Version = "2012-10-17",
                Statement = [
                {
                    Effect    = "Allow",
                    Principal = "*",
                    Action    = "*",
                    Resource  = "arn:aws:s3:::${aws_s3_bucket.example.id}/*"
                }
                ]
            })
}

