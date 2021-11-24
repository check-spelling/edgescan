from unittest import TestCase
from edgescan.data.types.vulnerability import Vulnerability
from tests.integration.api_client import get_api_client

import unittest


class VulnerabilityIntegrationTestCases(TestCase):
    edgescan_api = None

    @classmethod
    def setUpClass(cls):
        cls.edgescan_api = get_api_client()
        try:
            next(cls.edgescan_api.iter_vulnerabilities(limit=1))
        except StopIteration:
            raise unittest.SkipTest("No vulnerabilities found")

    def test_get_vulnerabilities(self):
        rows = self.edgescan_api.get_vulnerabilities()
        self.assertIsInstance(rows, list)
        self.assertGreater(len(rows), 0)
        self.assertTrue(all(isinstance(row, Vulnerability) for row in rows))

    def test_count_vulnerabilities(self):
        total = self.edgescan_api.count_vulnerabilities()
        self.assertGreater(total, 0)
