Colorifix-backend

Tech test for Colorifix

This the repositery for the database API and backend for the Colorifix test

The database is built with Sqlite, SQLalchemy.
The API is genarated with FastAPI. The logic is coded in Python3

API endpoints are created to be consumed on the Colorifix client created with React App.
The Aim is to create a User table with Company and Permission tables as Foreign Keys

Please clone the repository on your local machine and activate the virtual environment (venv)
Initialise the FasAPI swagger by typing in your terminal:

py -m uvicorn  --reload main:app

To access this URL:
http://localhost:8000/docs#/

Make sure the server is running 



