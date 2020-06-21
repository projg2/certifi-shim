#!/usr/bin/env python

import unittest

from certifi.core import contents


class CertifiShimTests(unittest.TestCase):
    def test_read_valid(self):
        """Assert that contents() read at least one certificate"""
        c = contents()
        self.assertIn('-----BEGIN CERTIFICATE-----', c)
        self.assertIn('-----END CERTIFICATE-----', c)


if __name__ == '__main__':
    unittest.main()
