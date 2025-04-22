import requests
import pytest
from config.config import BASE_URL, token
from config.payloads import (
    jsonUpdateGuest, jsonUpdateHall, jsonUpdateHallSchema,
    jsonCreateManagerReservation, jsonCreateCustomSchedule,
    jsonUpdateSettings
)
from utils.auth import BearerAuth

@pytest.mark.parametrize("url,json_payload", [
    (f"{BASE_URL}/api/Guests/UpdateGuest", jsonUpdateGuest),

    (f"{BASE_URL}/api/Halls/UpdateHallSchema",  jsonUpdateHallSchema),

    (f"{BASE_URL}/api/Halls/UpdateHall", jsonUpdateHall),

    (f"{BASE_URL}/api/Reservations/CreateManagerReservation", jsonCreateManagerReservation),

    (f"{BASE_URL}/api/Schedule/CreateCustomSchedule", jsonCreateCustomSchedule),

    (f"{BASE_URL}/api/RestaurantSettings/UpdateSettings", jsonUpdateSettings)
])

def test_post_endpoints(url, json_payload):
    response = requests.post(url, json=json_payload, auth=BearerAuth(token))
    assert response.status_code == 200, f"POST to {url} failed:\n{response.text}"
