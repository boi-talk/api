from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
  return "hello world"

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 8080))
  app.run(debug=False, host='0.0.0.0', port=port)
