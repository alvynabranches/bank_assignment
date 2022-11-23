resource "google_service_account" "service-prod" {
    account_id = "service-prod"
}

resource "google_project_iam_member" "service-prod" {
    project = "alvyn-kubernetes"
    role = "roles/storage.admin"
    member = "serviceAccount:${google_service_account.service-prod.email}"
}

resource "google_service_account_iam_member" "service-prod" {
    service_account_id = google_service_account.service-prod.id
    role = "roles/iam.workloadIdentityUser"
    member = "serviceAccount:alvyn-kubernetes.svc.id.goog[prod/service-prod]"
}