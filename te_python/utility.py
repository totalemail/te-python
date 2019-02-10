#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

import requests


def make_request(url, data=None, return_json=False):
    """Make a request to the given site."""
    response = requests.post(url, data=json.dumps(data))

    if not response.ok:
        message = 'ERROR: Got {} response from {}: {}'.format(response.status_code, url, response.text)
        print(message)
        return None
    else:
        return json.loads(response.text)
