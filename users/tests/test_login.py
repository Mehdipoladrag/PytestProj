import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestLogin:
    def test_login_page_loads(self, client):
        url = reverse("users:login")
        response = client.get(url)

        assert response.status_code == 200
        assert b"Login" in response.content

    def test_login_success(self, client, django_user_model):
        user = django_user_model.objects.create_user(
            username="testuser",
            password="StrongPass123"
        )

        url = reverse("users:login")
        response = client.post(url, {
            "username": "testuser",
            "password": "StrongPass123",
        })

        assert response.status_code == 302
        assert response.url == reverse("homepage")
        assert "_auth_user_id" in client.session

    def test_login_wrong_password(self, client, django_user_model):
        django_user_model.objects.create_user(
            username="testuser",
            password="StrongPass123"
        )

        url = reverse("users:login")
        response = client.post(url, {
            "username": "testuser",
            "password": "WrongPass123",
        })

        assert response.status_code == 200
        assert b"please enter a correct username and password" in response.content.lower()