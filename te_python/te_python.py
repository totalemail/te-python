#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python SDK for TotalEmail."""

import requests

from .utility import base_api_url, make_request, create_header


def email_submit(email_text, base_api_url=base_api_url):
    """Submit an email to TotalEmail for spam analysis."""
    url = base_api_url.format('emails')
    email_data = {"full_text": email_text}

    return make_request(requests.post, url, data=email_data)


def email_get_details(email_id, base_api_url=base_api_url):
    """Get details about the email with the given email ID."""
    url = base_api_url.format('emails/{}'.format(email_id))

    return make_request(requests.get, url)


def email_add_analysis(api_token, email_id, analysis_data, base_api_url=base_api_url):
    """(AUTHENTICATION REQUIRED) Create a new analysis result."""
    url = base_api_url.format('emails/{}/analysis'.format(email_id))
    headers = create_header(api_token)

    return make_request(requests.get, url, data=analysis_data, headers=headers)


def email_add_hash(api_token, email_id, hash_type, hash_value, base_api_url=base_api_url):
    """(AUTHENTICATION REQUIRED) Add a hash to the email."""
    url = base_api_url.format('emails/{}'.format(email_id))
    headers = create_header(api_token)

    return make_request(requests.put, url, data={hash_type: hash_value}, headers=headers)


def email_tlsh_hash(api_token, email_id, tlsh_hash, base_api_url=base_api_url):
    """(AUTHENTICATION REQUIRED) Add a TLSH hash to the email."""
    return email_add_hash(api_token, email_id, 'tlsh_hash', tlsh_hash)
