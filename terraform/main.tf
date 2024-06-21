# Google Cloud Provider

module "gcp-cloud-resume" {
  source = "./modules/gcp"

  bucket_name = "cloud-resume-src-bucket"
  zip_file_name = "cloud-resume-src.zip"
  zip_file_path = "./src"

  function_name = "cloud-resume"
  function_entry_point = "main.handler"
  function_runtime = "python312"

  firestore_database_name = "cloud-resume-nosql"
  firestore_location_id = "nam5"
}