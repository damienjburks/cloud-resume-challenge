resource "google_storage_bucket" "bucket" {
  name     = var.bucket_name
  location = "US"
}

resource "google_storage_bucket_object" "archive" {
  name   = var.zip_file_name
  bucket = google_storage_bucket.bucket.name
  source = var.zip_file_path
}

resource "google_cloudfunctions_function" "function" {
  name        = var.function_name
  description = var.function_description
  runtime     = var.function_runtime

  available_memory_mb   = 128
  source_archive_bucket = google_storage_bucket.bucket.name
  source_archive_object = google_storage_bucket_object.archive.name
  trigger_http          = true

  https_trigger_security_level = "SECURE_ALWAYS"
  entry_point                   = var.function_entry_point
}

resource "google_firestore_database" "database" {
  name                              = var.firestore_database_name
  location_id                       = var.firestore_location_id
  type                              = "FIRESTORE_NATIVE"
  concurrency_mode                  = "OPTIMISTIC"
  app_engine_integration_mode       = "DISABLED"
  point_in_time_recovery_enablement = "POINT_IN_TIME_RECOVERY_DISABLED"
  delete_protection_state           = "DELETE_PROTECTION_DISABLED"
  deletion_policy                   = "DELETE"
}

# IAM
resource "google_project_iam_custom_role" "custom_role" {
  role_id     = "customRoleId"
  title       = "Custom Role Title"
  description = "A custom role with specific permissions"
  permissions = [
    "storage.buckets.get",
    "storage.buckets.list",
    "storage.objects.get",
    "storage.objects.list"
  ]
}

output "custom_role_name" {
  value = google_project_iam_custom_role.custom_role.name
}