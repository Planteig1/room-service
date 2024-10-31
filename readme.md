# Rooms Service

This Flask-based microservice manages room availability, cleaning status, and provides a list of all rooms.

## Endpoints

- **Update room availability**

    - **URL**: `/room/availability`
    - **Method**: `PUT`
    - **Description**: Toggles the availability status of a room.
    - **Request Body**:

        ```json
        {
            "room_number": 101
        }
        ```

    - **Response**:
        - `200 OK`: Availability status updated successfully.
        - `400 Bad Request`: Unable to update availability or room not found.

- **Check room availability**

    - **URL**: `/room/availability`
    - **Method**: `GET`
    - **Description**: Checks the availability of a specific room.
    - **Query Parameters**:
        - `room_number`: The number of the room to check.
    - **Response**:
        - `200 OK`: Availability status of the room.
        - `400 Bad Request`: Room not found.

- **Get all rooms**

    - **URL**: `/rooms`
    - **Method**: `GET`
    - **Description**: Retrieves a list of all rooms.
    - **Response**:
        - `200 OK`: List of rooms.
        - `400 Bad Request`: No rooms found.

- **Get room type**

    - **URL**: `/room/type/<int:room_number>`
    - **Method**: `GET`
    - **Description**: Retrieves the type of a specific room.
    - **Response**:
        - `200 OK`: Type of the room.
        - `400 Bad Request`: Room not found.

- **Update cleaning status**

    - **URL**: `/room/cleaning`
    - **Method**: `PUT`
    - **Description**: Toggles the cleaning status of a room.
    - **Request Body**:

        ```json
        {
            "room_number": 101
        }
        ```

    - **Response**:
        - `200 OK`: Cleaning status updated successfully.
        - `400 Bad Request`: Unable to update cleaning status or room not found.

- **Send all room data**

    - **URL**: `/rooms/data`
    - **Method**: `GET`
    - **Description**: Retrieves all room data.
    - **Response**:
        - `200 OK`: List of all room data.
        - `400 Bad Request`: Error retrieving data.
