import json
import unittest

from project.tests.base import BaseTestCase

class TestInstances(BaseTestCase):
    """Tests for the API"""

    def test_get_single_instance(self):
        """Get single instance"""
        instance_id = "i-abc123"
        scope = "alphanumeric"
        with self.client:
            response = self.client.get("/instances/{instance_id}".format(instance_id=instance_id))
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn(instance_id, data["data"]["instance_id"])
            self.assertIn(scope, data["data"]["scope"])
            self.assertIn("success", data["status"])

    def test_single_instance_incorrect_id(self):
        """Ensure error is thrown if the id does not exist."""
        with self.client:
            response = self.client.get("/instances/i-dont-exist")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn("instance does not exist", data["message"])
            self.assertIn("fail", data["status"])    

    def test_get_instances_no_id(self):
        """Ensure error is thrown if an id is not provided."""
        with self.client:
            response = self.client.get("/instances/")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn("please specify instance id", data["message"])
            self.assertIn("fail", data["status"])

    def test_get_all_instances(self):
        """Ensure error is thrown if an id is not provided."""
        with self.client:
            response = self.client.get("/instances")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn("not implemented", data["message"])
            self.assertIn("fail", data["status"])

if __name__ == "__main__":
    unittest.main()