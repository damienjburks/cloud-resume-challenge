"""
This module contains a Flask route handler function for retrieving the resume data
and logging the request headers into a Firebase Firestore database.
"""

import os
import logging
import json

from firebase_admin import credentials, firestore, initialize_app

from google.cloud.logging import Client
from flask import Response, Request

# Setup Google Cloud Logging
Client().setup_logging(log_level=logging.INFO)

# Initialize Firebase Admin SDK
cred = credentials.ApplicationDefault()
initialize_app(cred)


def handler(request: Request):
    """
    This function handles the request and returns a JSON response containing the resume data.

    Args:
        request: The Flask request object.

    Returns:
        A JSON response containing the resume data and a 200 status code.
    """
    headers = dict(request.headers)
    log_data_into_firestore(headers)
    logging.info("Inserted headers into database for tracking and analytics...")

    with open("./assets/resume.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())

    return Response(
        response=json.dumps(data, sort_keys=False),
        status=200,
        mimetype="application/json",
    )


def log_data_into_firestore(headers: dict):
    """
    This function inserts the request headers into the Firebase Firestore database.

    Args:
        headers: A dictionary containing the request headers.
    """

    # Initialize Firestore client
    db = firestore.client()
    db_name = os.environ.get("FIRESTORE_DB_NAME").split("/")[-1]
    db._database_string_internal = f"projects/dsb-innovation-hub/databases/{db_name}"  # pylint: disable=protected-access
    db.collection("user_data").document().set(headers)
