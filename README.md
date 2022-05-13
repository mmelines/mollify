# Mollify
This is a little scaffold tool I made to do some of the routine work based on
some observations I made while working with Flask and SQLAlchemy. The goal is
to make the process of creating the aspects common to a CRUD Flask app a little 
faster with the goal of getting to "the good stuff" faster.

The primary goals of the app are to read a `model.py` file created by the user
and make the kind of API endpoints, forms and routes one might need with very
little front end styling or opininons. These starting points can then be 
modified by a developer with an understanding of Flask and extended based on 
intended use.

The backend has some built-in functions I found myself using repeatedly, and
these functions are quite opinionated. It might not be for everyone, but it's
how I would do it.

As it is currently designed, security and authorization features are not 
production-ready, and decisions have to be made here. `flask-login` is not
implemented here, but it can be implemented with the creation of an appropriate
`Users` entity, etc. Security features will likely be the first to become 
obselete anyways, and it is not currently practical for them to be maintained.

## Filetree

### In this repository
_
|- `reader.py`
|- `README.md`   *you are here*
|- `config.py`


### Generated after initial run

### Generated after succcessful `model.py` creation

## How To Use It
Clone this repo and open the mollify_config file to alter the name and 
specify your local database connection. 