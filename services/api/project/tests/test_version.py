import json
import unittest

from project.tests.base import BaseTestCase

class TestVersion(BaseTestCase):
    """Tests for the API"""

    def test_version(self):
        """Ensure the /version route works ok"""
        response = self.client.get("/version")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('1.0', data['version'])
        self.assertIn("success", data["status"])     

if __name__ == '__main__':
    unittest.main()