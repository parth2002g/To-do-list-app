
# Introduction

This is an API for a todo app. The API service is implemented using a REST-based architecture.

This app has the following main features:

- Create an item in the todo list
- Read the complete todo list
- Update the items with status as "Not Started", "In Progress", or "Complete"
- Delete the items from the list

# REST

REST, or REpresentational State Transfer, is an architectural style for building web services and APIs. It requires the systems implementing REST to be stateless. The client sends a request to the server to retrieve or modify resources without knowing what state the server is in. The servers send the response to the client without needing to know what was the previous communication with the client.

Each request to the RESTful system commonly uses these 4 HTTP verbs:

- **GET**: Get a specific resource or a collection of resources
- **POST**: Create a new resource
- **PUT**: Update a specific resource
- **DELETE**: Remove a specific resource

Although others are permitted and sometimes used, like PATCH, HEAD, and OPTIONS.

# FLASK

Flask is a framework for Python to develop web applications. It is non-opinionated, meaning that it does not make decisions for you. Because of this, it does not restrict to structure your application in a particular way. It provides greater flexibility and control to developers using it. Flask provides you with the base tools to create a web app, and it can be easily extended to include most things that you would need to include in your app.

# HOW TO USE THE APPLICATION

**Step 1** Clone the git repository into your system. Install the required packages from requirements.txt using the following command `pip install -r requirements.txt`.
**Step 2** Run `main.py` file by using the command `python main.py`.
**Step 3** Open a new command line tab while the program is running in the previous tab.
**Step 4** Use the following commands to do the operations.
## Adding items

    $ curl -X POST http://127.0.0.1:5000/item -d '{"item": "Setting up Flask"}' -H 'Content-Type: application/json'`
We should get the following response

   

    {"Setting up Flask": "Not Started"}
## Retrieving All Items

    $ curl -X GET http://127.0.0.1:5000/items/all

We should get the following response

    json {"count": 2, "items": [["Setting up Flask", "Not Started"], [Implement POST endpoint", "Not Started"]]}

## Getting Status of Individual Items

    $ curl -X GET http://127.0.0.1:5000/item/status?name=Setting+up+Flask

We should get the following response

    {"status": "Not Started"}
## Updating Items

    $ curl -X PUT http://127.0.0.1:5000/item/update -d '{"item": "Setting up Flask", "status": "Completed"}' -H 'Content-Type: application/json'

We should get the following response

    {"Setting up Flask": "Completed"}

## Deleting Items

    $ curl -X DELETE http://127.0.0.1:5000/item/remove -d '{"item": "Setting up Flask"}' -H 'Content-Type: application/json'

We should get the following response

    {"item": "Temporary item to be deleted"}

