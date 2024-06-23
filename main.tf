# Google Cloud Provider

module "gcp-cloud-resume" {
  source = "./tf-modules/gcp"

  bucket_name = "cloud-resume-src-bucket"
  function_src_dir = "${path.module}/serverless-src"
  zip_file_name = "cloud-resume-src"
  zip_file_path = "${path.module}/serverless-src.zip"

  function_name = "cloud-resume-api"
  function_entry_point = "handler"
  function_runtime = "python312"

  firestore_database_name = "cloud-resume-nosql"
  firestore_location_id = "nam5"
}