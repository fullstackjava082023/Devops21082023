provider "aws" {
  region = "us-east-1"  
}

resource "aws_iam_user" "arja" {
  name = "arja"
  tags = {
    "Position" = "None from the North"
  }
}

resource "aws_iam_policy" "s3_management" {
    name = "s3"
    description = "Allow s3 access"
    # policy = file("s3.json")
    policy = <<EOF
            {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "s3:*"
                    ],
                    "Resource": "*"
                }
            ]
        }
    EOF
}


resource "aws_iam_policy" "lambda_management" {
    name = "LambdaManagerPolicy"
    description =  "Custom policy to manage AWS Lambda functions"
    policy = file("lambda_policy.json")   
}

resource "aws_iam_user_policy_attachment" "add_admin" {
    user = aws_iam_user.arja.name
    policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}

resource "aws_iam_user_policy_attachment" "add_s3_manager" {
    user = aws_iam_user.arja.name
    policy_arn = aws_iam_policy.s3_management.arn
}

resource "aws_iam_user_policy_attachment" "add_lambda_manager" {
    user = aws_iam_user.arja.name
    policy_arn = aws_iam_policy.lambda_management.arn
}


resource "aws_iam_group" "starks" {
  name = "starks"
}

# add Arja to the starks group
resource "aws_iam_group_membership" "starks_team" {
  name = "starks_team"

  users = [
    aws_iam_user.arja.name,
    # aws_iam_user.user_two.name,
  ]

  group = aws_iam_group.starks.name
}

resource "aws_iam_group_policy_attachment" "lambda_attachment_to_group" {
  group      = aws_iam_group.starks.name
  policy_arn = aws_iam_policy.lambda_management.arn
}