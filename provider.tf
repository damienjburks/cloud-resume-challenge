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
    user = "damien"
    environment = "dev"
    project = "cloud-resume-challenge"
  }
}