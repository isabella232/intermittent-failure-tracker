# csc517ossproject

# Phase I Team:
* Erika Eill
* Zachary Taylor
* Adam Weber

# Phase II Team:
* Zachary Taylor
* Adam Weber
* Preston Scott
* John Crick

Intermittent tracker for servo

# Project description
* https://github.com/servo/servo/wiki/Tracking-intermittent-failures-over-time-project

# Inspired by 
* https://github.com/servo/intermittent-tracker

There are two major endpoints for this service, *record* and *query*.

# Record
This is the end point that will record a new entry into the database.  It requires the following parameters:
* test_file - the name of the testfile
* platform - the platform parameter
* builder - the test machine (builder)
* number - the github pull request number

# Query
This is the endpoint that will retrieve a result from the database.  It requires only one parameter
* filename - the name of the test file to retrieve


Instructions:
* `python flask_server.py [port]`

The database is stored in `static/intermittent_errors.json`.
