import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_logout(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="testuser",
        password="StrongPass123"
    )

    # login first
    client.login(username="testuser", password="StrongPass123")

    # logout
    response = client.post(reverse("users:logout"))

    assert response.status_code == 302
    assert response.url == reverse("users:login")

    # session should be cleared
    assert "_auth_user_id" not in client.session

