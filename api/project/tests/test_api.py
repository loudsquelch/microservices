import json
import unittest

from project.tests.base import BaseTestCase

class TestApi(BaseTestCase):
    """Tests for the API"""

    def test_api_version(self):
        """Ensure the /api/version route works ok"""
        response = self.client.get("/api/version")
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('1.0', data['version'])

if __name__ == '__main__':
    unittest.main()