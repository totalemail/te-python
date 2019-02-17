#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

import requests

base_api_url = 'https://totalemail.io/api/v1/{}'


def create_header(api_token=None):
    headers = {
        'Content-type': 'application/json'
    }

    if api_token:
        headers['Authorization'] = 'Token {}'.format(api_token)

    return headers


def make_request(function, url, data=None, return_json=True, api_token=None):
    """Make a request to the given site."""
    headers = create_header(api_token)

    if data:
        response = function(url, data=json.dumps(data), headers=headers)
    else:
        response = function(url, headers=headers)

    if not response.ok:
        message = 'ERROR: Got {} response from {}: {}'.format(response.status_code, url, response.text)
        print(message)
        return {'status': 'failure', 'message': message}
    else:
        if return_json:
            return {'status': 'success'}
        else:
            return response.text
