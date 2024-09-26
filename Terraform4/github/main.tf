terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = var.github_token
}


resource "github_repository" "terra-repository" {
  name        = "terra-repo"
  description = "A simple example repository"
  visibility = "public"
}

resource "github_branch" "development" {
  repository = github_repository.terra-repository.name
  branch     = "development"
}


resource "github_repository_webhook" "terra-webhook" {
  repository = github_repository.terra-repository.name
  events     = ["push"]
  configuration {
    url          = "http://www.shashkist.com/webhook"
    content_type = "json"
  }
}
