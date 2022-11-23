resource "google_service_account" "service-staging" {
    account_id = "service-staging"
}

resource "google_project_iam_member" "service-staging" {
    project = "alvyn-kubernetes"
    role = "roles/storage.admin"
    member = "serviceAccount:${google_service_account.service-staging.email}"
}

resource "google_service_account_iam_member" "service-staging" {
    service_account_id = google_service_account.service-staging.id
    role = "roles/iam.workloadIdentityUser"
    member = "serviceAccount:alvyn-kubernetes.svc.id.goog[prod/service-staging]"
}