from unittest import TestCase
from edgescan.data.types.host import Host
from tests.integration.api_client import get_api_client

import unittest


class HostIntegrationTestCases(TestCase):
    edgescan_api = None

    @classmethod
    def setUpClass(cls):
        cls.edgescan_api = get_api_client()
        try:
            next(cls.edgescan_api.iter_hosts(limit=1))
        except StopIteration:
            raise unittest.SkipTest("No hosts found")

    def test_get_hosts(self):
        rows = self.edgescan_api.get_hosts()
        self.assertIsInstance(rows, list)
        self.assertGreater(len(rows), 0)
        self.assertTrue(all(isinstance(row, Host) for row in rows))

    def test_count_hosts(self):
        total = self.edgescan_api.count_hosts()
        self.assertGreater(total, 0)
