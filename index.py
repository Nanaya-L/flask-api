from flask import Flask, render_template, request, jsonify
import pickle
import os

app = Flask(__name__, template_folder='templates')
port = os.getenv("PORT")
admin = os.getenv("admin")
adminPassword = os.getenv("password")

dt_model = pickle.load(open('./ML_Models/finalized_dt_model.sav', 'rb'))
knn_model = pickle.load(open('./ML_Models/finalized_knn_model.sav', 'rb'))
svm_model = pickle.load(open('./ML_Models/finalized_svm_model.sav', 'rb'))

if admin == None:
    admin = "admin"

if adminPassword == None:
    adminPassword = "123456"

def validateVars(vars):
    for var in vars:
        if(vars[var]== ''):
            return True
    return False
        
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


@app.route("/predict/model", methods=["POST"])
def predict():
    data = request.form
    validVars = validateVars(data)
    if validVars == True:
        return render_template('mainPage.html')

    # ph	Hardness	Solids	Chloramines	Sulfate	Conductivity	Organic_carbon	Trihalomethanes	Turbidity
    ph = data["ph"]
    Hardness = data["Hardness"]
    Solids = data["Solids"]
    Chloramines = data["Chloramines"]
    Sulfate = data["Sulfate"]
    Conductivity = data["Conductivity"]
    Organic_carbon = data["Organic_carbon"]
    Trihalomethanes = data["Trihalomethanes"]
    Turbidity = data["Turbidity"]

    print([[float(ph), float(Hardness), float(Solids), float(Chloramines), float(Sulfate), float(
        Conductivity), float(Organic_carbon), float(Trihalomethanes), float(Turbidity)]])

    knn_result = knn_model.predict(
        [[float(ph), float(Hardness), float(Solids), float(Chloramines), float(Sulfate), float(Conductivity), float(Organic_carbon), float(Trihalomethanes), float(Turbidity)]])

    dt_result = dt_model.predict(
        [[float(ph), float(Hardness), float(Solids), float(Chloramines), float(Sulfate), float(Conductivity), float(Organic_carbon), float(Trihalomethanes), float(Turbidity)]])

    svm_result = svm_model.predict(
        [[float(ph), float(Hardness), float(Solids), float(Chloramines), float(Sulfate), float(Conductivity), float(Organic_carbon), float(Trihalomethanes), float(Turbidity)]])

    template_data = {
        'knn_result': str(knn_result),
        'dt_result': str(dt_result),
        'svm_result': str(svm_result)
        }
    #return jsonify(knn_result=str(knn_result), dt_result=str(dt_result), svm_result=str(svm_result))
    return render_template('response.html', **template_data)

if port == None:
    port = 5000

print(port)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)
