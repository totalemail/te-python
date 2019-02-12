#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
import utility

BASE_API_URL = 'https://totalemail.io/api/v1/{}'


def domain_add(domain, related_item_type, related_item_id):
    url = BASE_API_URL.format('domains')
    data = {
        "domain_name": domain
    }

    return utility.make_request(requests.post, url, data=data)


def email_address_add(email_address, related_item_type, related_item_id):
    url = BASE_API_URL.format('email_addresses')
    data = {
        "email_address": email_address
    }

    return utility.make_request(requests.post, url, data=data)


def ipv4_add(ip_address, related_item_type, related_item_id):
    url = BASE_API_URL.format('ip_addresses')
    data = {
        "ipv4": ip_address
    }

    return utility.make_request(requests.post, url, data=data)


def url_add(network_data_url, related_item_type, related_item_id):
    url = BASE_API_URL.format('urls')
    data = {
        "url": network_data_url
    }

    return utility.make_request(requests.post, url, data=data)
