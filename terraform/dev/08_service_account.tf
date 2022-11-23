resource "google_service_account" "service-dev" {
    account_id = "service-dev"
}

resource "google_project_iam_member" "service-dev" {
    project = "alvyn-kubernetes"
    role = "roles/storage.admin"
    member = "serviceAccount:${google_service_account.service-dev.email}"
}

resource "google_service_account_iam_member" "service-dev" {
    service_account_id = google_service_account.service-dev.id
    role = "roles/iam.workloadIdentityUser"
    member = "serviceAccount:alvyn-kubernetes.svc.id.goog[prod/service-dev]"
}