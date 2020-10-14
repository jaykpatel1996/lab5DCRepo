#!/usr/bin/env python3

import argparse
import os
import time
from pprint import pprint

import googleapiclient.discovery
import google.auth
import requests


credentials, project = google.auth.default()

service = googleapiclient.discovery.build('compute', 'v1', credentials=credentials)

PROJECT = "crypto-symbol-288101"

ZONE = 'us-west1-b' 

# Name of the instance scoping this request.
INSTANCE = 'instance2'  # TODO: Update placeholder value.

t = service.instances().get(project=PROJECT,zone=ZONE,instance=INSTANCE).execute()
fingerprint = t["labelFingerprint"]


tags_body = {
    "items": [
    "allow-5000"
  ],
  "fingerprint":fingerprint
}

request = service.instances().setTags(project=PROJECT, zone=ZONE, instance=INSTANCE, body=tags_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)


