#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .utility import make_post_request


def domain_add(domain, headers, bodies):
    """(AUTHENTICATION REQUIRED) Create a domain in TotalEmail."""
    url_path = 'domains/'
    data = {'host_name': domain, 'headers': headers, 'bodies': bodies}

    return make_post_request(url_path, data)


def email_address_add(email_address, headers, bodies):
    """(AUTHENTICATION REQUIRED) Create an email address in TotalEmail."""
    url_path = 'emailAddresses/'
    data = {'email_address': email_address, 'headers': headers, 'bodies': bodies}

    return make_post_request(url_path, data)


def ipv4_add(ip_address, headers, bodies):
    """(AUTHENTICATION REQUIRED) Create an ip address in TotalEmail."""
    url_path = 'ipAddresses/'
    data = {'ip_address': ip_address, 'headers': headers, 'bodies': bodies}

    return make_post_request(url_path, data)


def url_add(network_data_url, headers, bodies):
    """(AUTHENTICATION REQUIRED) Create a URL in TotalEmail."""
    url_path = 'urls/'
    data = {'url': network_data_url, 'bodies': bodies}

    return make_post_request(url_path, data)
