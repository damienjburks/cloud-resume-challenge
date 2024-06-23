"""
This module contains a Flask route handler function for retrieving the resume data.
"""

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

    with open("./assets/resume.json", "r") as f:
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
    db._database_string_internal = (
        "projects/dsb-innovation-hub/databases/cloud-resume-nosql"
    )
    db.collection("user_data").document().set(headers)
