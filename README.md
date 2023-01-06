# Development

## Setup

1. Make a .env file in the root folder

```
DATABASE_URL="PUT YOUR LOCAL DATABASE URL HERE"
```

2. Create a virtual environment

```bash
python3 -m venv venv
```

3. Activate the virtual environment

```bash
. venv/bin/activate
```

4. Install requirements (Flask)

```bash
pip install -r requirements.txt
```

## Database Migrations (using flask-migrate look at the docs)

Useful commands
`flask db upgrade`
`flask db downgrade`

## Running Locally

To run do this
`flask run`

# Deployment

`fly deploy`
