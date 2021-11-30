from edgescan.data.types.license import License

import tests.api_client as client
import unittest


class LicenseTestCases(unittest.TestCase):
    edgescan_api = None

    @classmethod
    def setUpClass(cls):
        cls.edgescan_api = client.get_api_client()
        try:
            next(cls.edgescan_api.iter_licenses(limit=1))
        except StopIteration:
            raise unittest.SkipTest("No licenses found")

    def test_get_licenses(self):
        rows = self.edgescan_api.get_licenses()
        self.assertIsInstance(rows, list)
        self.assertGreater(len(rows), 0)
        self.assertTrue(all(isinstance(row, License) for row in rows))

    def test_count_licenses(self):
        total = self.edgescan_api.count_licenses()
        self.assertGreater(total, 0)
