import pytest
from website.models import Record

@pytest.mark.django_db
def test_record_creation():
    record = Record.objects.create(
        first_name='Jane',
        last_name='Smith',
        email='jane@example.com',
        phone='0987654321',
        address='456 Oak Ave',
        city='Othertown',
        state='NY',
        zipcode='54321'
    )
    assert record.first_name == 'Jane'

def test_record_fields():
    record = Record()
    assert record._meta.get_field('first_name').max_length == 50
    assert record._meta.get_field('last_name').max_length == 50
    assert record._meta.get_field('email').max_length == 100