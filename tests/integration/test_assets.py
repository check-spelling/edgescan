from unittest import TestCase
from edgescan.api.client import EdgeScan
from edgescan.data.types.asset import Asset

import unittest


class AssetIntegrationTestCases(TestCase):
    edgescan_api = None

    @classmethod
    def setUpClass(cls):
        cls.edgescan_api = EdgeScan()
        try:
            next(cls.edgescan_api.iter_assets(limit=1))
        except StopIteration:
            raise unittest.SkipTest("No assets found")

    def test_get_assets(self):
        rows = self.edgescan_api.get_assets()
        self.assertIsInstance(rows, list)
        self.assertGreater(len(rows), 0)
        self.assertTrue(all(isinstance(row, Asset) for row in rows))

    def test_count_assets(self):
        total = self.edgescan_api.count_assets()
        self.assertGreater(total, 0)
