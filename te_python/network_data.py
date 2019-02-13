#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
import utility


def domain_add(domain, headers, bodies):
    """(AUTHENTICATION REQUIRED) Create a domain in TotalEmail."""
    url = utility.BASE_API_URL.format('domains')
    data = {
        'host_name': domain,
        'headers': headers,
        'bodies': bodies
    }

    return utility.make_request(requests.post, url, data=data)


def email_address_add(email_address, headers, bodies):
    """(AUTHENTICATION REQUIRED) Create an email address in TotalEmail."""
    url = utility.BASE_API_URL.format('emailAddresses')
    data = {
        'email_address': email_address,
        'headers': headers,
        'bodies': bodies
    }

    return utility.make_request(requests.post, url, data=data)


def ipv4_add(ip_address, headers, bodies):
    """(AUTHENTICATION REQUIRED) Create an ip address in TotalEmail."""
    url = utility.BASE_API_URL.format('ipAddresses')
    data = {
        'ip_address': ip_address,
        'headers': headers,
        'bodies': bodies
    }

    return utility.make_request(requests.post, url, data=data)


def url_add(network_data_url, headers, bodies):
    """(AUTHENTICATION REQUIRED) Create a URL in TotalEmail."""
    url = utility.BASE_API_URL.format('urls')
    data = {
        'url': network_data_url,
        'bodies': bodies
    }

    return utility.make_request(requests.post, url, data=data)
