from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder='templates')
port = os.getenv("PORT")
admin = os.getenv("admin")
adminPassword = os.getenv("password")

if admin == None:
    admin = "admin"

if adminPassword == None:
    adminPassword = "123456"


@app.route('/', methods=['GET'])
def hello():
    return render_template('login.html')


@app.route("/api/login", methods=["POST"])
def login():
    data = request.form
    username = data["username"]
    password = data["password"]

    # Validar os dados de login

    if username == admin and password == adminPassword:
        return render_template('mainPage.html')
    else:
        return render_template('unauthorized.html')


if port == None:
    port = 5000

print(port)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)
