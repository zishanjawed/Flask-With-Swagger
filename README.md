# Flask REST API with Swagger and SQLAlchemy

This is a Flask REST API project that uses Swagger for API documentation and SQLAlchemy for interacting with a SQL database. The API allows you to manage people and their associated notes.

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

##  Configuration

Configure the database connection and other settings by modifying the config.py file.

```bash
# config.py

SQLALCHEMY_DATABASE_URI = '<your-database-uri>'
```

## Usage

To start the Flask server, run the following command:

```bash
python app.py

```

Configure the database connection and other settings by modifying the config.py file.

```bash
# config.py

SQLALCHEMY_DATABASE_URI = '<your-database-uri>'
```
The server will be running at http://localhost:5000.



## API Documentation

The API documentation is generated using Swagger. You can access the Swagger UI by visiting http://localhost:5000/api/ui.

###  Endpoints
The following endpoints are available:

#### People
    . GET /api/people: Get the list of all people.
    . POST /api/people: Create a new person.
    . GET /api/people/{lname}: Get information about a specific person.
    . PUT /api/people/{lname}: Update information about a specific person.
    . DELETE /api/people/{lname}: Delete a specific person.

#### Notes
    . POST /api/notes: Create a new note associated with a person.
    . GET /api/notes/{note_id}: Get information about a specific note.
    . PUT /api/notes/{note_id}: Update information about a specific note.
    . DELETE /api/notes/{note_id}: Delete a specific note.

Refer to the Swagger documentation for detailed information about the request and response formats for each endpoint.

## Database Schema
The following is the schema for the Person model:
```python
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(255))
    lname = db.Column(db.String(255), nullable=False)
```
## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please create a new issue or submit a pull request.

## License

[MIT](https://choosealicense.com/licenses/mit/)