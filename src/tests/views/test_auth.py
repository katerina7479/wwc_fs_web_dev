from rest_framework import status
from rest_framework.test import APITestCase
import json


class AuthUserTests(APITestCase):
    def test_register(self):
        """
        Ensure we can register a new user
        """
        url = "/auth/registration/"
        data = {
            "first_name": "Admin",
            "last_name": "User",
            "password": "my99pAssword!",
            "email": "email@example.com",
        }

        response = self.client.post(url, data, format="json")
        content = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(content["first_name"], "Admin")
        self.assertEqual(content["is_active"], True)

    def test_register_with_bad_email(self):
        """
        Ensure that registration with a bad email fails
        """
        url = "/auth/registration/"
        data = {
            "first_name": "Admin",
            "last_name": "User",
            "password": "my99password!",
            "email": "bad email",
        }
        response = self.client.post(url, data, format="json")
        content = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            content["email"],
            [
                "The email address bad email is not valid",
                "Enter a valid email address.",
            ],
        )

    def test_register_with_bad_password(self):
        """
        Ensure that registration with a bad password fails
        """
        url = "/auth/registration/"
        data = {
            "first_name": "Admin",
            "last_name": "User",
            "password": "1234",
            "email": "email@example.com",
        }
        response = self.client.post(url, data, format="json")
        content = response.json()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(len(content["password"]), 4)


class LoginTests(APITestCase):
    def setUp(self):
        url = "/auth/registration/"
        self.email = "email@example.com"
        self.password = "my1Password7&"
        data = {
            "first_name": "Admin",
            "last_name": "User",
            "password": self.password,
            "email": self.email,
        }
        self.client.post(url, data, format="json")

    def test_jwt_auth(self):
        """
        Ensure we can authenticate with JWT and get a refresh token.
        """
        url = "/auth/login/"
        data = {"email": self.email, "password": self.password}
        response = self.client.post(url, data, format="json")
        content = response.json()
        # Verify that the response has a 200 status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verify that a token is returned
        self.assertIn("access", content)
        self.assertIn("refresh", content)

    def test_jwt_refresh(self):
        """
        Ensure we can refresh the JWT.
        """
        # Log in first
        url = "/auth/login/"
        data = {"email": self.email, "password": self.password}
        response = self.client.post(url, data, format="json")

        # Verify that the response has a 200 status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = response.json()
        # Verify that a token is returned
        self.assertIn("access", content)
        self.assertIn("refresh", content)

        url = "/auth/token/refresh/"
        data = {"refresh": content["refresh"]}
        response = self.client.post(url, data, format="json")

        content = response.json()
        self.assertIn("access", content)
        self.assertNotIn("refresh", content)
