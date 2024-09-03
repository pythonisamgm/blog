# Diario de Miguel

This project is a personal blog called "Diario de Miguel". It is built using Flask and allows users to view blog posts, learn more about the author, and send messages through a contact form.

## Features

- **Home Page**: Displays a list of blog posts with the number of days and notes.
- **About Page**: Provides information about the author.
- **Contact Page**: Allows users to send a message to the author.
### Special Features

- **JSON Data Handling**: The application opens a JSON file (`babyplus_data_export.json`) and loads its content. This JSON contains blog post data, including dates and notes.
  
- **Dynamic Picture Handling**: For each blog post, the application:
  - Takes the date from the post and calculates the number of days since a specific date (Miguel's birthdate).
  - If a post does not have an associated picture, the application selects a random image from a predefined folder (`static/assets/img/dev`) and links it to the post.

## Setup

### Requirements

- Python 3.8 or higher
- Flask
- Flask-Mail (for sending emails)
### Installation

To set up this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/diario-de-miguel.git
    cd diario-de-miguel
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root directory of the project and add your configuration settings.

    Example:
    ```bash
    FLASK_APP=app.py
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
   
    ```

5. **Run the application**:
    ```bash
    flask run
    ```

The application will be accessible at `http://127.0.0.1:5000`.

## Contact Page

The contact form on the Contact Page is set up to send emails to the specified email address in your configuration. Ensure that your email service is correctly configured in the `.env` file.

Example configuration for Gmail:
```bash
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=1
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_email_password
MAIL_DEFAULT_SENDER=your_email@gmail.com
```
### Project Structure
- templates/: Contains HTML templates for web pages.
- static/: Contains static files like CSS, JavaScript, and images.
- app.py: The main file of the Flask application.
- config.py: Application configurations.
- models.py: Data model definitions.
- routes.py: Route definitions.
- requirements.txt: List of project dependencies.
