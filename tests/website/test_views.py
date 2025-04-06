import pytest
from django.urls import reverse
from website.models import Record
from django.contrib.auth import get_user_model

User = get_user_model()

# --- Fixtures ---

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='testpass')

@pytest.fixture
def record(db):
    return Record.objects.create(
        first_name='John',
        last_name='Doe',
        email='john@example.com',
        phone='1234567890',
        address='123 Main St',
        city='Anytown',
        state='CA',
        zipcode='12345'
    )

# --- Tests ---

@pytest.mark.django_db
def test_home_view_authenticated(client, user):
    client.force_login(user)
    response = client.get(reverse('home'))
    assert response.status_code == 200
    assert 'records' in response.context

@pytest.mark.django_db
def test_home_view_unauthenticated(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_register_view_get(client):
    response = client.get(reverse('register'))
    assert response.status_code == 200
    assert 'form' in response.context

@pytest.mark.django_db
def test_customer_record_view_authenticated(client, user, record):
    client.force_login(user)
    response = client.get(reverse('record', args=[record.id]))
    assert response.status_code == 200
    assert 'customer_record' in response.context

@pytest.mark.django_db
def test_customer_record_view_unauthenticated(client, record):
    response = client.get(reverse('record', args=[record.id]))
    assert response.status_code == 302  # Redirect to login page
