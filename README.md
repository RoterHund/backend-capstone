# Back End Capstone

## Description

This project serves as the backend implementation for a restaurant management system. It provides various endpoints to manage menu items and bookings, along with authentication features.

## API Endpoints

### Menu Items

- **GET and POST:** Retrieve and create menu items.
  - Endpoint: `restaurant/menu-items`
  - Authentication: Not required

- **GET, PUT, DELETE:** Retrieve, update, and delete individual menu items.
  - Endpoint: `restaurant/menu-items/<id>`
  - Authentication: Token required

### Bookings

- **GET and POST:** Retrieve and make bookings for tables.
  - Endpoint: `restaurant/booking/tables/`
  - Authentication: Token required

## Authentication

- **Browsable API:** Use the Browsable API to interactively add new users.

- **Generate Token:** 
  - Endpoint: `auth/token/login/`
  - Method: POST
  - Description: Generate token for registered users.

- **Logout User:** 
  - Endpoint: `auth/token/logout/`
  - Method: POST
  - Description: Logout the user.

### Additional Endpoints

- **Generate API Token:** 
  - Endpoint: `restaurant/api-token-auth/`
  - Method: POST
  - Description: Generate a token.

## Testing

To run tests located in the `tests` folder, execute the following command:

```bash
python manage.py test tests
