#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python SDK for TotalEmail."""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
import utility

BASE_API_URL = 'https://totalemail.io/api/v1/{}'


def email_submit(email_text):
    """Submit an email to TotalEmail for spam analysis."""
    url = BASE_API_URL.format('emails')
    email_data = {
        "full_text": email_text
    }

    return utility.make_request(url, data=email_data, return_json=True)


def email_get_details(email_id):
    """Get details about the email with the given email ID."""
    url = BASE_API_URL.format('emails/{}'.format(email_id))

    return utility.make_request(url)
