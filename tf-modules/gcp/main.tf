data "archive_file" "function_src" {
  type             = "zip"
  source_dir       = var.function_src_dir
  output_file_mode = "0666"
  output_path      = var.zip_file_path
}

resource "google_storage_bucket" "bucket" {
  name     = var.bucket_name
  location = "US"
}

resource "google_storage_bucket_object" "src" {
  name   = "${var.zip_file_name}_${data.archive_file.function_src.output_md5}.zip"
  bucket = google_storage_bucket.bucket.name
  source = data.archive_file.function_src.output_path
}

resource "google_cloudfunctions_function" "function" {
  name        = var.function_name
  description = var.function_description
  runtime     = var.function_runtime

  available_memory_mb   = 128
  source_archive_bucket = google_storage_bucket.bucket.name
  source_archive_object = google_storage_bucket_object.src.name
  trigger_http          = true

  https_trigger_security_level = "SECURE_ALWAYS"
  entry_point                  = var.function_entry_point
}

# Allow the function to be invoked from the HTTP from all users
resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = google_cloudfunctions_function.function.project
  region         = google_cloudfunctions_function.function.region
  cloud_function = google_cloudfunctions_function.function.name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"

  depends_on = [ google_cloudfunctions_function.function ]
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
