"""
This module contains a Flask route handler function for retrieving the resume data.
"""

import logging
import json
from flask import Response

# Initialize the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def handler(request):
    """
    This function handles the request and returns a JSON response containing the resume data.
    
    Args:
        request: The Flask request object.
        
    Returns:
        A JSON response containing the resume data and a 200 status code.
    """
    with open("./assets/resume.json", 'r') as f:
        data = json.loads(f.read())

    return Response(
        response=json.dumps(data, sort_keys=False),
        status=200,
        mimetype='application/json'
    )