# Citation Extraction Django Application

This project is a Django web application that fetches data from a paginated API, processes the responses to identify the sources, and presents the results in a user-friendly format. The application includes a simple UI to display the results and an API endpoint to get the citations as JSON.

## Features

- Fetch data from a paginated API.
- Identify whether the response for each response-sources pair came from any of the sources.
- List the sources from which the response was formed (citations).
- Present the citations for all objects coming from the API through a web interface.
- Provide a JSON API to access the citations programmatically.

## Technologies Used

- Python
- Django
- HTML

## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/citation_project.git
   cd citation_project
Create a Virtual Environment:

sh
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

sh
Copy code
pip install -r requirements.txt
Apply Migrations:

sh
Copy code
python manage.py migrate
Run the Server:

sh
Copy code
python manage.py runserver
Access the Application:

Open your web browser and navigate to http://127.0.0.1:8000/ to see the citations. You can also access the API at http://127.0.0.1:8000/api/citations/.