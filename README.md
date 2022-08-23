Tech test for Colorifix 1/2

1/Colorifix-backend


This the repositery for the database API and backend for the Colorifix test

The database is built with Sqlite, SQLalchemy.
The API is generated with FastAPI. The logic is coded in Python3

API endpoints are created to be consumed on the Colorifix client created with React App.
The Aim is to create a User table with Company and Permission tables as Foreign Keys

Please clone the repository on your local machine and activate the virtual environment (venv)
Initialise the FasAPI swagger by typing in your terminal:

py -m uvicorn main:app

To access this URL:
http://localhost:8000/docs#/

Make sure the colorifix-backend server is running so the API end points are consumed on the Client side

Clone the React app Colorifix-frontend
https://github.com/helenemartin/colorifix-frontend

TODO

.Clear cached git files from the repo

.Fix bugs: I can't assign a company to a user:
sqlalchemy.exc.InterfaceError: (sqlite3.InterfaceError) Error binding parameter 1 - probably unsupported type.

[SQL: INSERT INTO user (username, company_id) VALUES (?, ?)]
[parameters: ('raddish@yahoo.co.uk', <db.models.DbCompany object at 0x0000013629D63DF0>)]

.Fix the User end point to be properly consumed on the React app in order to list users

.Create a persmission table in order to assign user roles

