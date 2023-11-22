from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
def hello():
    return render_template('login.html')


@app.route("/api/login", methods=["POST"])
def login():

    data = request.form
    username = data["username"]
    password = data["password"]

    # Validar os dados de login

    if username == "admin" and password == "123456":
        return {"status": "success"}
    else:
        return {"status": "error"}


port = os.getenv("PORT")


if port == None:
    port = 5000

print(port)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)
