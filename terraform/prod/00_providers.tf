provider "google" {
    project = "alvyn-kubernetes"
    region = "us-central1-a"
}

locals {
    project = "alvyn-kubernetes"
}

terraform {
    # backend "gcs" {
    #     bucket = "app-deploy-prod"
    #     prefix = "terraform/state"
    # }

    required_providers {
        google = {
            source = "hashicorp/google"
            version = "~> 4.0"
        }
    }
}