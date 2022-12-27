import json
from flask import Flask, jsonify
from models import db, User
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

db.init_app(app)

with app.app_context():
    db.create_all()



@app.route("/")
def index():
  return "hello world"

@app.route("/users")
def users():
  # test_user = User(email="testemail",password="testpass")
  # db.session.add(test_user)
  # db.session.commit()

  users = User.query.all()
  res = []
  for user in users:
    dict = {
      "email":user.email,
      "password":user.password
    }
    res.append(dict)

  return jsonify(res)

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 8080))
  app.run(debug=True, host='0.0.0.0', port=port)
