#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    import ConfigParser
except:
    import configparser as ConfigParser
import json
import os

try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse

import requests

CONFIG_FILE_PATH = os.path.expanduser('~') + '/.totalemail/conf'
DEFAULT_BASE_API_URL = 'https://totalemail.io/api/v1/'


def _read_config_file(config_file_path):
    """Read the config file with configuration details."""
    api_token = None
    api_base_url = DEFAULT_BASE_API_URL

    config = ConfigParser.RawConfigParser()
    with open(config_file_path) as f:
        config.read_file(f)

    default_config = config['default']

    if default_config.get('api_token'):
        api_token = default_config['api_token']

    if default_config.get('api_base_url'):
        api_base_url = default_config['api_base_url']

    return api_token, api_base_url


def init(config_file_path=CONFIG_FILE_PATH):
    """Collect the data required to make a request to TE."""
    headers = {'Content-type': 'application/json'}

    api_token, api_base_url = _read_config_file(config_file_path)

    if api_token:
        headers['Authorization'] = 'Token {}'.format(api_token)

    if api_base_url is None:
        message = 'The api_base_url entry in the config file ({}) has no value. Please provide a valid value or remove the api_base_url entry to use the default API ({}).'.format(
            CONFIG_FILE_PATH, DEFAULT_BASE_API_URL
        )
        raise RuntimeError(message)
    else:
        # if there is a api_base_url, make sure it ends with a '/'
        if not api_base_url.endswith('/'):
            api_base_url = api_base_url + '/'

    return headers, api_base_url


def make_get_request(url_path):
    """Make a GET request to the given URL."""
    url = urlparse.urljoin(base_api_url, url_path)
    response = requests.get(url, headers=headers)
    return response


def make_post_request(url_path, data):
    """Make a POST request to the given URL."""
    url = urlparse.urljoin(base_api_url, url_path)
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response


def make_put_request(url_path, data):
    """Make a PUT request to the given URL."""
    url = urlparse.urljoin(base_api_url, url_path)
    response = requests.put(url, data=json.dumps(data), headers=headers)
    return response


headers, base_api_url = init()
