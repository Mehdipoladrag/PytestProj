import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestSignup:
    def test_signup_page_loads(self, client):
        url = reverse("users:signup")
        response = client.get(url)

        assert response.status_code == 200
        assert b"Registration" in response.content

    def test_signup_success(self, client, django_user_model):
        url = reverse("users:signup")

        response = client.post(url, {
            "username": "testuser",
            "email": "testuser@test.com",
            "password1": "StrongPass123",
            "password2": "StrongPass123",
        })

        assert response.status_code == 302
        assert response.url == reverse("homepage")

        assert django_user_model.objects.filter(
            username="testuser"
        ).exists()

        assert "_auth_user_id" in client.session

    def test_signup_password_mismatch(self, client):
        url = reverse("users:signup")

        response = client.post(url, {
            "username": "testuser2",
            "email": "test2@test.com",
            "password1": "StrongPass123",
            "password2": "WrongPass123",
        })

        assert response.status_code == 200
        assert b"password" in response.content.lower()

    def test_signup_duplicate_email(self, client, django_user_model):
        django_user_model.objects.create_user(
            username="existing",
            email="dup@test.com",
            password="StrongPass123"
        )

        url = reverse("users:signup")
        response = client.post(url, {
            "username": "newuser",
            "email": "dup@test.com",
            "password1": "StrongPass123",
            "password2": "StrongPass123",
        })

        assert response.status_code == 200
        assert b"email" in response.content.lower()
