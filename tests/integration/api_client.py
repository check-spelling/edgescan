from edgescan.api.client import EdgeScan
from edgescan.errors import MissingCredentialsError

import unittest


def get_api_client():
    try:
        return EdgeScan()
    except MissingCredentialsError:
        raise unittest.SkipTest("No API key provided")
