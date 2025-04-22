import pytest

def random_date_string():
    date = datetime.today() + timedelta(days=random.randint(0, 10))
    return date.strftime("%d-%m-%Y")

def random_year():
    return random.randint(2023, 2025)

def random_month():
    return random.randint(1, 12)
    
@pytest.fixture(scope="module")
def shared_ids():
    return {
        "hallId": 128,
        "schemaId": 147,
        "reservationId": "08dd8060-5a0c-4ba3-80f8-7c402448045d",
        "restaurantId": 24,
        "tableId": 66,
        "email": "random@random.com",
        "date": random_date_string(),
        "dateTime": "2025-04-21T14:30:00Z",
        "year": random_year(),
        "month": random_month()
    }

@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json"
    }
