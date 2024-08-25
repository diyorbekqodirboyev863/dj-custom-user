# Django Custom User Model

This project demonstrates how to implement a custom user model in Django with custom fields and user management. It includes:

- Custom user model (`CustomUser`) with email-based authentication.
- A `Rank` model to manage user ranks with various attributes.
- Custom user creation and management forms using `django-crispy-forms`.
- Basic views for user registration and login.
- Custom error pages for common HTTP errors.

## Features

- **Custom User Model**: Extends `AbstractBaseUser` and `PermissionsMixin` to create a user model with custom fields.
- **Rank Model**: Manages user ranks with fields for rank type, level, description, and score.
- **User Registration**: Users can register with email and password.
- **User Login**: Users can log in using their email and password.
- **Error Handling**: Custom pages for HTTP 400 (Bad Request) and HTTP 500 (Server Error) errors.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/diyorbekqodirboyev863/dj-custom-user.git
   cd dj-custom-user
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000` to see the application in action.

## Usage

- **Register**: Navigate to `/register/` to create a new user account.
- **Login**: Navigate to `/login/` to log in with your email and password.

## Customizing

You can customize the `Rank` model and the `CustomUser` model by modifying their respective fields and methods in `models.py`.

## Error Pages

Custom error pages for HTTP 400 and HTTP 500 errors are included. You can customize these pages in `templates/400.html` and `templates/500.html`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django framework for providing a robust and flexible web framework.
- `django-crispy-forms` for simplifying form rendering in Django.
