#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

from .utility import base_api_url, make_request, create_header


def domain_add(api_token, domain, headers, bodies, base_api_url=base_api_url):
    """(AUTHENTICATION REQUIRED) Create a domain in TotalEmail."""
    url = base_api_url.format('domains')
    data = {'host_name': domain, 'headers': headers, 'bodies': bodies}
    headers = create_header(api_token)

    return make_request(requests.post, url, data=data, headers=headers)


def email_address_add(api_token, email_address, headers, bodies, base_api_url=base_api_url):
    """(AUTHENTICATION REQUIRED) Create an email address in TotalEmail."""
    url = base_api_url.format('emailAddresses')
    data = {'email_address': email_address, 'headers': headers, 'bodies': bodies}
    headers = create_header(api_token)

    return make_request(requests.post, url, data=data, headers=headers)


def ipv4_add(api_token, ip_address, headers, bodies, base_api_url=base_api_url):
    """(AUTHENTICATION REQUIRED) Create an ip address in TotalEmail."""
    url = base_api_url.format('ipAddresses')
    data = {'ip_address': ip_address, 'headers': headers, 'bodies': bodies}
    headers = create_header(api_token)

    return make_request(requests.post, url, data=data, headers=headers)


def url_add(api_token, network_data_url, headers, bodies, base_api_url=base_api_url):
    """(AUTHENTICATION REQUIRED) Create a URL in TotalEmail."""
    url = base_api_url.format('urls')
    data = {'url': network_data_url, 'bodies': bodies}
    headers = create_header(api_token)

    return make_request(requests.post, url, data=data, headers=headers)
