from psycopg2.errors import UniqueViolation
from flask import Flask, jsonify, request
from models import User
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from email_validator import validate_email, EmailNotValidError
import os
import bcrypt

load_dotenv(find_dotenv())

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL").replace("postgres://", "postgresql://", 1)
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


@app.route("/user", methods=["POST"])
def register():
    data = request.get_json(force=True)

    if ("email" not in data) or ("password" not in data):
        return jsonify({"error": "No email or password field"}), 400

    email = data["email"]
    password = data["password"]

    if (email == None or email == "") or (password == None or password == ""):
        return jsonify({"error": "Must provide email and password"}), 400

    try:
      # validate and get info
        validate_email(email)
    except EmailNotValidError:
        # email is not valid
        return jsonify({"error": "invalid email"}), 400

    hashed_pass = bcrypt.hashpw(
        bytes(password, encoding='utf-8'), bcrypt.gensalt())
    new_user = User(
        email=email,
        password=hashed_pass
    )

    try:
        db.session.add(new_user)
        db.session.commit()
    except UniqueViolation:
        return jsonify({"error": "User with email already exists"}), 409
    except:
        return jsonify({"error": "Internal error"}), 500

    return jsonify({"success": "User created"}), 200
