from flask import Flask, jsonify, request
from models import User
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from email_validator import validate_email, EmailNotValidError
import hashlib
import os

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
    email = data["email"]
    password = data["password"]
    if len(email)==0 and len(password)==0:
        return "Email and password are empty",400

    try:
      # validate and get info
        validate_email(email)
    except EmailNotValidError:
        # email is not valid
        return "invalid email", 400

    if len(password)==0:
        return jsonify({"error":"invalid password"}), 400

    user = User.query.filter_by(email=email).first()
    if user:
        return "User with email already exists", 409

    hashed_pass = hashlib.sha256(str.encode(password)).hexdigest()
    new_user = User(
        email=email,
        password=hashed_pass
    )

    db.session.add(new_user)
    db.session.commit()

    return "User created", 200




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=False, host='0.0.0.0', port=port)
