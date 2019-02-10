#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

import requests


def create_header(api_token):
    return {'Authorization': 'Token {}'.format(api_token)}


def make_request(function, url, data=None, headers={}, return_json=True):
    """Make a request to the given site."""
    if data:
        response = function(url, data=json.dumps(data), headers=headers)
    else:
        response = function(url, headers=headers)

    if not response.ok:
        message = 'ERROR: Got {} response from {}: {}'.format(response.status_code, url, response.text)
        print(message)
        return {
            'status': 'failure',
            'message': message
        }
    else:
        if return_json:
            results = json.loads(response.text)
            results['status'] = 'success'
            return results
        else:
            return response.text
