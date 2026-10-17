import unittest
from app import app


class AppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_returns_project_details(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("OC CI/CD Final Project", response.get_json()["project"])

    def test_health_returns_ok(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")


if __name__ == "__main__":
    unittest.main()
