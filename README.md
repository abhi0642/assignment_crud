# Assignment CRUD

This is a Django REST API project that provides endpoints for user registration, login, and product management. It includes authentication using JWT tokens and role-based authorization for product CRUD operations.

## Features

- User registration: Allows users to register with a unique username, email, password, and role.
- User login: Authenticates users and provides JWT tokens for authorization.
- Product CRUD: Provides endpoints for creating, reading, updating, and deleting products. Access to these endpoints is restricted based on user roles.
- JWT authentication: Uses JWT tokens for authentication and authorization of API requests.

## Technologies Used

- Python
- Django
- Django REST Framework
- JWT (JSON Web Tokens)
- SQLite (or your chosen database)

## Installation

1. Clone the repository:
git clone https://github.com/abhi0642/assignment_crud.git 

2. Install the required dependencies:

pip install -r requirements.txt


3. Run database migrations:

python manage.py migrate


4. Start the development server:


python manage.py runserver


5. Access the API endpoints locally at [http://localhost:8000/](http://localhost:8000/).

## API Endpoints

- `/api/register`: POST endpoint for user registration. Requires fields: username, email, password, role.
- `/api/login`: POST endpoint for user login. Requires fields: email, password.
- `/api/products`: GET endpoint to retrieve all products. Requires a valid JWT token for authorization.
- `/api/products/{id}`: GET, PUT, DELETE endpoints to retrieve, update, or delete a specific product. Requires a valid JWT token for authorization.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to open an issue or submit a pull request.
