import pytest

@pytest.fixture(scope="module")
def shared_ids():
    return {
        "hallId": 128,
        "schemaId": 147,
        "reservationId": "08dd8060-5a0c-4ba3-80f8-7c402448045d",
        "restaurantId": 24,
        "tableId": 66,
        "email": "random@random.com",
        "date": "01-01-2024",
        "dateTime": "2025-04-21T14:30:00Z",
        "year": 2025,
        "month": 4
    }

@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json"
    }
