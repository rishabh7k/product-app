## ShopEase

This is a Django-based web application for managing products and users. The application allows users to register, log in, view products in different layouts (grid, list, card), and manage their accounts.

## Prerequisites

- Python 3.8+
- Django 5.0.9
- HTML/CSS
- Microsoft SQL Server

## Technology Stack

- Backend: Django
- Frontend: HTML, CSS, JavaScript
- Database: Microsoft SQL Server
- Authentication: Django's built-in authentication system

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/rishabh7k/product-app.git
cd product-app
```

### 2. Create and Activate a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Set Up Database Connection

Update the database settings in `settings.py`

```py
DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": "{Your Database Name}",
        "HOST": "{Your SQL Server Host}",
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server",
            "Trusted_Connection": "yes",
        },
    }
}
```

### 5. Apply Migrations

```sh
python manage.py makemigrations
python manage.py migrate
```

### 6. Configure `.env`.

Configure a `.env` based on `.env.example` provided, and place it in project root, with `manage.py`.

```env
FAKER_API_URL=https://fakerapi.it/api/v2/products
FAKER_API_QUANTITY=10
```

### 7. Run the Development Server

```sh
python manage.py runserver
```

### 8. Access the Application

Open your web browser and go to `http://127.0.0.1:8000`.

## Demo

[Watch the video on YouTube](https://www.youtube.com/watch?v=VZMGY-7N7BE)

## Additional Information

- The application uses Django's built-in authentication system with a custom user model defined in `users/models.py`.

- Product views are implemented in `products/views.py` and templates are located in `products/templates`.

- User-related views and forms are implemented in `users/views.py` and `users/forms.py`.

For any issues or contributions, please open an issue or submit a pull request on the [GitHub repository](https://github.com/rishabh7k).
