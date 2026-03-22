from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pickle
import os
import numpy as np

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

model = pickle.load(open("model/crop_model.pkl","rb"))


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/predict",methods=["POST"])
def predict():

    data = request.form

    def safe_int(val, default=0):
        try:
            return int(float(val))
        except (ValueError, TypeError):
            return default

    def safe_float(val, default=0.0):
        try:
            return float(val)
        except (ValueError, TypeError):
            return default

    N = safe_int(data.get("N"))
    P = safe_int(data.get("P"))
    K = safe_int(data.get("K"))
    temperature = safe_float(data.get("temperature"))
    humidity = safe_float(data.get("humidity"))
    ph = safe_float(data.get("ph"))
    rainfall = safe_float(data.get("rainfall"))

    input_data=np.array([[N,P,K,temperature,humidity,ph,rainfall]])

    prediction=model.predict(input_data)[0]

    return render_template("result.html", prediction=prediction, inputs=data)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
