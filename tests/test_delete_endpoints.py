import pytest
import requests
from config.config import BASE_URL, token
from utils.auth import BearerAuth

@pytest.mark.parametrize("name,path", [
    ("DeleteHall", "/api/Halls/DeleteHall?hallId={hallId}"),
    ("DeleteSchema", "/api/Halls/DeleteSchema?schemaId={schemaId}"),
    ("DeleteReservation", "/api/Reservations/DeleteReservation?reservationId={reservationId}"),
    ("DeleteCustomSchedule", "/api/Schedule/DeleteCustomSchedule?scheduleId={scheduleId}")
])
def test_delete_requests(name, path, shared_ids, token):
    url = BASE_URL + path.format(**shared_ids)
    response = requests.delete(url, auth=BearerAuth(token))
    assert response.status_code in (200, 204), f"{name} failed: {response.status_code}\n{response.text}"
