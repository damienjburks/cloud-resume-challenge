"""
This module contains a Flask route handler function for retrieving the resume data
and logging the request headers into a Firebase Firestore database.
"""

import os
import logging
import json

from firebase_admin import credentials, firestore, initialize_app

from google.cloud.logging import Client as GLoggingClient
from google.cloud.storage import Client as GStorageClient
from flask import Response, Request

# Setup Google Cloud Clients
GLoggingClient().setup_logging(log_level=logging.INFO)
storage_client = GStorageClient()

# Initialize Firebase Admin SDK
cred = credentials.ApplicationDefault()
initialize_app(cred)
db = firestore.client()
db_name = os.environ["FIRESTORE_DB_NAME"].split("/")[-1]
db._database_string_internal = f"projects/dsb-innovation-hub/databases/{db_name}"  # pylint: disable=protected-access


def call_return_list_of_objects():
    """
    This function calls a placeholder function that returns a list of objects
    in a Cloud Storage bucket.
    """
    return (
        json.dumps(_return_list_of_objects),
        200,
        {"Content-Type": "application/json"},
    )


def handler(request: Request):
    """
    This function handles the request and returns a JSON response containing the resume data.

    Args:
        request: The Flask request object.

    Returns:
        A JSON response containing the resume data and a 200 status code.
    """
    logging.info("Calling function: %s", _return_list_of_objects())

    headers = dict(request.headers)
    log_data_into_firestore(headers)
    logging.info("Inserted headers into database for tracking and analytics...")

    data = get_latest_resume()
    logging.info("Retrieved latest resume data from database...")

    return Response(
        response=json.dumps(data, sort_keys=False),
        status=200,
        mimetype="application/json",
    )


def get_latest_resume():
    """
    This function retrieves the latest resume data from the Firebase Firestore database.

    Returns:
        A dictionary containing the latest resume data.
    """
    # Get the latest document from the "resumes" collection
    docs = db.collection("resumes").stream()

    latest_doc_dict = None
    for doc in docs:
        latest_doc_dict = doc.to_dict()

    return latest_doc_dict


def log_data_into_firestore(headers: dict):
    """
    This function inserts the request headers into the Firebase Firestore database.

    Args:
        headers: A dictionary containing the request headers.
    """
    db.collection("user_data").document().set(headers)


def _return_list_of_objects():
    """
    This function is a placeholder for a function that returns a list of objects
    in a Cloud Storage bucket.
    """
    buckets = storage_client.list_buckets()
    return {"listOfBuckets": [bucket.name for bucket in buckets]}
