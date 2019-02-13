#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python SDK for TotalEmail."""

import os
import sys

import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
import utility


def email_submit(email_text):
    """Submit an email to TotalEmail for spam analysis."""
    url = utility.BASE_API_URL.format('emails')
    email_data = {
        "full_text": email_text
    }

    return utility.make_request(requests.post, url, data=email_data)


def email_get_details(email_id):
    """Get details about the email with the given email ID."""
    url = utility.BASE_API_URL.format('emails/{}'.format(email_id))

    return utility.make_request(requests.get, url)


def email_add_analysis(api_token, email_id, analysis_data):
    """(AUTHENTICATION REQUIRED) Create a new analysis result."""
    url = utility.BASE_API_URL.format('emails/{}/analysis'.format(email_id))
    headers = utility.create_header()

    return utility.make_request(requests.get, url, data=analysis_data, headers=headers)


def email_add_hash(api_token, email_id, hash_type, hash_value):
    """(AUTHENTICATION REQUIRED) Add a hash to the email."""
    url = utility.BASE_API_URL.format('emails/{}'.format(email_id))
    headers = utility.create_header()

    return utility.make_request(requests.put, url, data={
        hash_type: hash_value
    }, headers=headers)


def email_tlsh_hash(api_token, email_id, tlsh_hash):
    """(AUTHENTICATION REQUIRED) Add a TLSH hash to the email."""
    return email_add_hash(api_token, email_id, 'tlsh_hash', tlsh_hash)
