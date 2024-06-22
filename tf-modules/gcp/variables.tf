variable "bucket_name" {
  type = string
}

variable "function_src_dir" {
  type = string
}

variable "zip_file_name" {
  type = string
}

variable "zip_file_path" {
  type = string
}

variable "function_name" {
  type = string
}

variable "function_runtime" {
  type = string
}

variable "function_description" {
  type = string
  default = null
}

variable "function_entry_point" {
  type = string
}

variable "firestore_database_name" {
  type = string
}

variable "firestore_location_id" {
  type = string
}