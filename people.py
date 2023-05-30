
from flask import abort, make_response
from config import db
from models import Person, people_schema, person_schema


def read_all():
    """
    The function reads all instances of the Person model and returns them as a serialized JSON object
    using the people_schema.
    :return: The function `read_all()` is returning a serialized list of all the `Person` objects in the
    database using the `people_schema` schema.
    """
    people = Person.query.all()
    return people_schema.dump(people)

def create(person):
    """
    The function creates a new person in the database if they do not already exist, otherwise it returns
    an error message.
    
    :param person: The `person` parameter is a dictionary containing information about a person, such as
    their first name, last name, and age. It is used to create a new `Person` object in the database if
    a person with the same last name does not already exist. If a person with the same last
    :return: If a new person is successfully created and added to the database, the function will return
    the newly created person's information in JSON format along with a status code of 201 (created). If
    a person with the same last name already exists in the database, the function will return an HTTP
    error response with a status code of 406 (not acceptable) and a message indicating that a person
    with that last
    """
    lname = person.get("lname")
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person is None:
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(406, f"Person with last name {lname} already exists")

def read_one(lname):
    """
    This function reads a person's information from a database based on their last name and returns it
    in a serialized format, or raises a 404 error if the person is not found.
    
    :param lname: lname is a string variable representing the last name of a person. It is used as a
    parameter in the function `read_one` to query the database for a person with the specified last
    name. If a person with the specified last name is found, their information is returned in JSON
    format using the `
    :return: The function `read_one` returns the serialized data of a person with the specified last
    name if found in the database, using the `person_schema.dump()` method. If the person is not found,
    it raises a 404 error with a message indicating that the person with the specified last name was not
    found.
    """
    person = Person.query.filter(Person.lname == lname).one_or_none()

    if person is not None:
        return person_schema.dump(person)
    else:
        abort(404, f"Person with last name {lname} not found")
    

def update(lname, person):
    """
    This function updates an existing person's first name based on their last name.
    
    :param lname: lname is a string parameter representing the last name of a person. It is used to
    query the database for an existing person with the same last name
    :param person: The `person` parameter is a dictionary or JSON object containing the updated
    information for a person. It is passed to the `update()` function to update the existing person with
    the matching last name (`lname`). The `person` dictionary should have keys that match the attributes
    of the `Person` model,
    :return: If an existing person with the given last name is found, the function updates the person's
    first name and returns the updated person's information as a JSON object with a status code of 201.
    If no person with the given last name is found, the function aborts with a 404 error message.
    """
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        update_person = person_schema.load(person, session=db.session)
        existing_person.fname = update_person.fname
        db.session.merge(existing_person)
        db.session.commit()
        return person_schema.dump(existing_person), 201
    else:
        abort(404, f"Person with last name {lname} not found")

def delete(lname):
# This code is deleting a person from the database based on their last name. It first queries the
# database for a person with the specified last name using `Person.query.filter(Person.lname ==
# lname).one_or_none()`. If a person with the specified last name is found, their information is
# stored in the `existing_person` variable. If `existing_person` is not `None`, the function deletes
# the person from the database using `db.session.delete(existing_person)` and commits the changes
# using `db.session.commit()`. It then returns a response indicating that the person was successfully
# deleted with a status code of 200. If `existing_person` is `None`, the function aborts with a 404
# error message indicating that the person with the specified last name was not found in the database.
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"{lname} successfully deleted", 200)
    else:
        abort(404, f"Person with last name {lname} not found")
