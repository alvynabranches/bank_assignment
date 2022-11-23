provider "google" {
    project = "alvyn-kubernetes"
    region = "us-central1"
}

locals {
    project = "alvyn-kubernetes"
}

terraform {

    required_providers {
        google = {
            source = "hashicorp/google"
            version = "~> 4.0"
        }
    }
}