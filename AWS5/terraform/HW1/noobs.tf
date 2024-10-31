provider "aws" {
  region = "us-east-1"  
}


resource "aws_iam_user" "newbie" {
  name = "newbie"
}

resource "aws_iam_user" "pro" {
  name = "pro"
}

resource "aws_iam_user_policy_attachment" "add_admin" {
    user = aws_iam_user.pro.name
    policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}

# add user to the noobs group
resource "aws_iam_group_membership" "noobs_members" {
  name = "noobs_members"

  users = [
    aws_iam_user.newbie.name,
    aws_iam_user.pro.name
    
  ]

  group = aws_iam_group.noobs.name
}


# add read s3 access to the noobs group
resource "aws_iam_group" "noobs" {
  name = "noobs"
}

# add read s3 access to the noobs group
resource "aws_iam_group_policy_attachment" "s3_read_attachment" {
  group      = aws_iam_group.noobs.name
  policy_arn = aws_iam_policy.s3_read.arn
}

# create policy add read s3 access 
resource "aws_iam_policy" "s3_read" {
  name = "s3_read"
  description = "Allow s3 read access"
  policy = <<EOF
          {
          "Version": "2012-10-17",
          "Statement": [
              {
                  "Effect": "Allow",
                  "Action": [
                      "s3:GetObject",
                      "s3:ListBucket"
                  ],
                  "Resource": "*"
              }
          ]
      }
  EOF
}

