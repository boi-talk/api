# Development

## Setup

Make a .env file in the root folder
Put this in there
`export DATABASE_URL="PUT YOUR LOCAL DATABASE URL HERE"`

Install requirements (Flask)

`pip install -r requirements.txt`

## Database Migrations (using flask-migrate look at the docs)

Useful commands
`flask db upgrade`
`flask db downgrade`

## Running Locally

To run do this
`flask run`

# Deployment

`fly deploy`
