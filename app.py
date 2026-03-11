from flask import Flask
from calculator import add

app = Flask(__name__)

@app.route("/")
def home():
    result = add(5,3)
    return f"CI/CD Python App Running. 5 + 3 = {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)