from flask import Flask, jsonify
from models import User
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

load_dotenv(find_dotenv())

db_url = os.getenv("DATABASE_URL")
db_url = db_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)


@app.route("/")
def index():
    return "hello world"


@app.route("/users")
def users():
    users = User.query.all()
    res = []
    for user in users:
        dict = {
            "email": user.email,
            "password": user.password
        }
        res.append(dict)

    return jsonify(res)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, host='0.0.0.0', port=port)
