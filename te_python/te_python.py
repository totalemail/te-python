#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python SDK for TotalEmail."""

from .utility import make_get_request, make_post_request, make_put_request


def email_submit(email_text):
    """Submit an email to TotalEmail for spam analysis."""
    url_path = '/emails'
    email_data = {"full_text": email_text}

    return make_post_request(url_path, email_data)


def email_get_details(email_id):
    """Get details about the email with the given email ID."""
    url_path = 'emails/{}/'.format(email_id)

    return make_get_request(url_path)


def email_add_analysis(email_id, analysis_notes, analysis_source, score=0):
    """(AUTHENTICATION REQUIRED) Create a new analysis result."""
    url_path = 'emails/{}/analysis/'.format(email_id)
    data = {'notes': analysis_notes, 'source': analysis_source, 'email': email_id, 'score': score}

    return make_post_request(url_path, data)


def email_add_hash(email_id, hash_type, hash_value):
    """(AUTHENTICATION REQUIRED) Add a hash to the email."""
    url_path = 'emails/{}/'.format(email_id)
    data = {hash_type: hash_value}

    return make_put_request(url_path, data)


def email_tlsh_hash(email_id, tlsh_hash):
    """(AUTHENTICATION REQUIRED) Add a TLSH hash to the email."""
    return email_add_hash(email_id, 'tlsh_hash', tlsh_hash)
