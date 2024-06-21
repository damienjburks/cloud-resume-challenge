terraform {
  cloud {
    organization = "DSB"

    workspaces {
      name = "cloud-resume-challenge"
    }
  }
}

provider "google" {
  project = "dsb-innovation-hub"
  region  = "us-central1"
  
  default_labels = {
    user = "Damien"
    email = "damien@damienjburks.com"
    environment = "dev"
    project = "cloud-resume-challenge"
    github_link = "https://github.com/damienjburks/cloud-resume-challenge"
  }
}