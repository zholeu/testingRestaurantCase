from datetime import datetime, timedelta

jsonUpdateHallSchema = {
                             "hallId": 128,
                             "schemaId": 147,
                             "tables": [
                                 {
                                     "id": 0,
                                     "x": 0,
                                     "y": 0,
                                     "height": 0,
                                     "width": 0,
                                     "name": "string",
                                     "maxCountOfGuests": 0,
                                     "minCountOfGuests": 0,
                                     "rotation": 0,
                                     "type": 0
                                 }
                             ],
                             "walls": [
                                 {
                                     "id": 0,
                                     "x": 0,
                                     "y": 0,
                                     "height": 0,
                                     "width": 0,
                                     "rotation": 0,
                                     "isCircle": "true"
                                 }
                             ],
                             "texts": [
                                 {
                                     "id": 0,
                                     "x": 0,
                                     "y": 0,
                                     "size": 0,
                                     "content": "string",
                                     "isVertical": "true",
                                     "rotation": 0
                                 }
                             ],
                             "ellipses": [
                                 {
                                     "id": 0,
                                     "x": 0,
                                     "y": 0,
                                     "height": 0,
                                     "width": 0
                                 }
                             ]
                         }
jsonUpdateGuest= {
        "id": 12535,
        "name": "Test Guest",
        "phone": "123456",
        "comment": "pytest update",
        "isFavorite": True
    }
jsonUpdateHall = {
        "hallId": 128,
        "activeSchemaId": 0,
        "hallName": "string",
        "isDisabled": True,
        "isDisabledForOnlineReserves": True
}
jsonCreateManagerReservation = {
        "phone": "pytest",
        "name": "Py Guest",
        "guests": 2,
        "time": datetime.utcnow().isoformat() + "Z",
        "note": "pytest note",
        "guestNote": "guest note",
        "isFavoriteGuest": True,
        "isTablesLocked": True,
        "duration": "15:00:00",
        "isCancelledByAdmin": False,
        "isStarted": False,
        "isConfirmed": True,
        "isFinishedByAdmin": False,
        "tableId": [0]
}
jsonCreateUserReservation = {
    "reservationId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "restaurantId": 24,
    "reservedAtDateTime": "2025-04-15T20:10:09.086Z",
    "guestName": "string",
    "guestPhone": "string",
    "guestCount": 0,
    "note": "string"
}
jsonUpdateReservation = {
    "phone": "string",
    "name": "string",
    "guests": 0,
    "time": "2025-04-15T20:14:51.472Z",
    "note": "string",
    "guestNote": "string",
    "isFavoriteGuest": "true",
    "isTablesLocked": "true",
    "duration": "15:00:00",
    "isCancelledByAdmin": "true",
    "isStarted": "true",
    "isConfirmed": "true",
    "isFinishedByAdmin": "true",
    "tableId": [
        0
    ],
    "reservationId": "08dd7c58-62a7-4980-8886-b13ec2221dd5"
}
jsonUpdateSettings = {
    "RestaurantSettingsDto": {
        "Name": "string",
        "address": "string",
        "webSite": "string",
        "description": "string",
        "phone": "string",
        "isAutoConfirm": "true",
        "isAutoManagerConfirm": "true",
        "isOverBookingEnabled": "true",
        "isNoTablesBookingDisabled": "true",
        "isAutoSelectTable": "true",
        "waitingDuration": {
            "ticks": 0
        },
        "timeBeforeReservation": {
            "ticks": 0
        },
        "timeBetweenReservations": {
            "ticks": 0
        },
        "notificationToken": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "maxCountOfGuests": 0,
        "timeZone": "2025-04-21T00:02:35Z"
    }

}
jsonUpdateSchedule = {
  "isOpen": "true",
  "isDefaultSchemas": "true",
  "startReservationsTime": {
    "ticks": 0
  },
  "stopReservationsTime": {
    "ticks": 0
  },
  "reservationDuration": {
    "ticks": 0
  },
  "durationUntilClose": "true",
  "hallsSchemas": [
    0
  ],
  "note": "string",
  "id": 0
}
jsonCreateCustomSchedule = {
        "ScheduleDTO": {
            "isOpen": True,
            "isDefaultSchemas": True,
            "startReservationsTime": { "ticks": 0 },
            "stopReservationsTime": { "ticks": 2340 },
            "reservationDuration": { "ticks": 200 },
            "durationUntilClose": True,
            "hallsSchemas": [0],
            "note": "pytest schedule",
            "dateFrom": datetime.utcnow().isoformat() + "Z",
            "dateTo": (datetime.utcnow() + timedelta(days=5)).isoformat() + "Z"
        }
}
