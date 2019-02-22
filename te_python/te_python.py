#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python SDK for TotalEmail."""

import requests

from .utility import base_api_url, make_request


def email_submit(email_text, base_api_url=base_api_url):
    """Submit an email to TotalEmail for spam analysis."""
    url = base_api_url.format('emails')
    email_data = {"full_text": email_text}

    return make_request(requests.post, url, data=email_data)


def email_get_details(email_id, base_api_url=base_api_url):
    """Get details about the email with the given email ID."""
    url = base_api_url.format('emails/{}'.format(email_id))

    return make_request(requests.get, url)


def email_add_analysis(api_token, email_id, analysis_notes, analysis_source, base_api_url=base_api_url):
    """(AUTHENTICATION REQUIRED) Create a new analysis result."""
    url = base_api_url.format('emails/{}/analysis'.format(email_id))

    data = {
        'notes': analysis_notes,
        'source': analysis_source,
        'email': email_id,
        'score': 0  # for now, this value is unimportant
    }

    return make_request(requests.post, url, data=data, api_token=api_token)


def email_add_hash(api_token, email_id, hash_type, hash_value, base_api_url=base_api_url):
    """(AUTHENTICATION REQUIRED) Add a hash to the email."""
    url = base_api_url.format('emails/{}'.format(email_id))

    return make_request(requests.put, url, data={hash_type: hash_value}, api_token=api_token)


def email_tlsh_hash(api_token, email_id, tlsh_hash, base_api_url=base_api_url):
    """(AUTHENTICATION REQUIRED) Add a TLSH hash to the email."""
    return email_add_hash(api_token, email_id, 'tlsh_hash', tlsh_hash, base_api_url=base_api_url)
