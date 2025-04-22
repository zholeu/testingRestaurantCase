import requests
import pytest
from config.config import BASE_URL, token
from fixtures.common_fixtures import shared_ids
from utils.auth import BearerAuth

@pytest.mark.parametrize("name,path", [
    ("RestaurantInfo", "/api/BaseInfo/RestaurantInfo"),
    ("GetGuests", "/api/Guests/GetGuests"),
    ("GetHallSchema", "/api/Halls/GetHallSchema?hallId={hallId}&schemaId={schemaId}"),
    ("RestaurantUsers", "/api/BaseInfo/RestaurantUsers"),
    ("GetTablesInfo", "/api/Main/GetTablesInfo?hallId={hallId}&schemaId={schemaId}&dateTime={dateTime}"),
    ("GetReservations", "/api/Reservations/GetReservations"),
    ("GetReservationInfo", "/api/Reservations/GetReservationInfo?reservationId={reservationId}"),
    ("ToggleClosingTable", "/api/Reservations/ToggleClosingTable?tableId={tableId}"),
    ("GetRestaurantInfo", "/api/Reservations/GetRestaurantInfo?restaurantId={restaurantId}"),
    ("GetClientReservationInfo", "/api/Reservations/GetClientReservationInfo?reservationId={reservationId}"),
    ("CancellReservation", "/api/Reservations/CancellReservation?reservationId={reservationId}"),
    ("SendReservationEmail", "/api/Reservations/SendReservationEmail?reservationId={reservationId}&email={email}"),
    ("GetAvailableDays", "/api/Reservations/GetAvailableDays?year={year}&month={month}&restaurantId={restaurantId}"),
    ("GetAvailableTimes", "/api/Reservations/GetAvailableTimes?restaurantId={restaurantId}"),
    ("GetAvailableGuests", "/api/Reservations/GetAvailableGuests?restaurantId={restaurantId}"),
    ("GetTableStatus", "/api/Reservations/GetTableStatus"),
    ("GetXlsReserves", "/api/Info/GetXlsReserves"),
    ("GetStatistics", "/api/Info/GetStatistics?date={date}"),
    ("GetSettings", "/api/RestaurantSettings/GetSettings"),
    ("GetMonthSchedule", "/api/Schedule/GetMonthSchedule?year={year}&month={month}"),
    ("GetDailySchedule", "/api/Schedule/GetDailySchedule?date={dateTime}")
])

def test_get_requests_sequential(name, path, shared_ids):
    url = BASE_URL + path.format(**shared_ids)
    response = requests.get(url, auth=BearerAuth(token))
    assert response.status_code == 200, f"{name} failed: {response.status_code}\n{response.text}"
