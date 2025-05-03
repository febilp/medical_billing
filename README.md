# Medical Inventory Management System

This system provides a comprehensive solution for managing medicines, bills, and inventory. The application includes APIs for CRUD operations on medicines, bill generation, sales reports, and stock availability. It also includes detailed API documentation using Swagger for easy reference.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Error Handling](#error-handling)
- [License](#license)

## Installation

### Prerequisites
- Python 3.x
- Django
- DRF (Django Rest Framework)
- drf-spectacular (for Swagger support)
- PostgreSQL (or any other database of your choice)

### Step-by-Step Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/febilp/medical_inventory_management.git
   cd medical_inventory_management

2. Create a Python virtual environment:
   ```bash
   python -m venv venv
3. Activate the virtual environment:
      -On Windows
      ```bash
      .\venv\Scripts\activate

4. Install the required dependencies:
      ```bash
      pip install -r requirements.txt
5. Apply migrations to set up the database:
      ```bash
      python manage.py migrate
6. Create a superuser for the admin panel and select role "staff" manually from django panel
       ```bash
   
         python manage.py createsuperuser

7. Run the server
   ```bash
   python manage.py runserver

Configuration
Database Setup: Ensure your DATABASES settings in settings.py are configured for your preferred database 

Swagger: The system uses drf-spectacular for auto-generating Swagger documentation. Once the server is running, you can access the API documentation at:

http://localhost:8000/api/swagger/

Authentication: The system uses token-based authentication. You can use Django’s built-in user authentication or extend it for your specific needs.

Usage
API Endpoints
The system exposes the following API endpoints:

1. Medicine CRUD APIs
POST /api/medicines/: Add a new medicine.

GET /api/medicines/: List all medicines.

GET /api/medicines/{id}/: Get medicine details by ID.

PUT /api/medicines/{id}/: Update medicine details.

DELETE /api/medicines/{id}/: Delete a medicine.

2. Bill APIs
POST /api/bills/: Create a new bill.

GET /api/bills/{id}/: Get bill details by ID.

3. Dashboard APIs (Admin Only)
GET /api/dashboard/stock/: Get available stock of all medicines.

GET /api/dashboard/reports/: Generate sales reports based on date range and staff-wise billing.

4. User APIs
POST /api/users/: Create a new user (admin only).

GET /api/users/{id}/: Retrieve user details.

PUT /api/users/{id}/: Update user details.

DELETE /api/users/{id}/: Delete a user.

Authentication
The API uses token-based authentication. You can obtain a token by making a POST request to the auth/token/ endpoint with your credentials. Then, include this token in the Authorization header of subsequent requests.
     ```bash
     
     Authorization: Bearer <your_token_here>

Swagger Documentation
The API is documented using Swagger. You can access the Swagger UI at:
      ```bash
      
         http://localhost:8000/api/swagger/

Error Handling
The API provides consistent error responses in the following format:

      
      {"error": "Error message describing the issue."}

      
Common errors include:

400 Bad Request: Missing or invalid data.

404 Not Found: Resource not found (e.g., invalid ID).

401 Unauthorized: Missing or invalid token.

Example Requests
1. Create Bill
URL: /api/bills/

Method: POST

Request Body:
      
      {
       "medicine_id": 1,
        "quantity": 2,
     "packaging_type": "piece"
      }
Response:
   
            {
     "medicine_id": 1,
     "quantity": 2,
     "packaging_type": "piece",
     "total_price": 150.0
      }
2. . Get Available Stock
URL: /api/dashboard/stock/

Method: GET

Response:
                        
      {
     "medicine_id": 1,
     "medicine_name": "Aspirin",
     "available_stock": 50
      }







