from flask import Flask, render_template, request

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


port = app.config.from_envvar(variable_name="PORT")


if __name__ == '__main__':
    app.run(port=port, debug=True)
