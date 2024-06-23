output "function_url" {
    value = google_cloudfunctions_function.function.https_trigger_url
    description = "The URL of the Cloud Function"
}