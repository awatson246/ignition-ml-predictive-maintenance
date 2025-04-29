from flask import Flask, request, jsonify
import joblib

model = joblib.load('model.pkl')

app = Flask(__name__)

# when a POST request is sent to endpoint (/predict), 
# function under @app.route is called
@app.route('/predict', methods=['POST'])

def predict():
    try:
        # gets temp and vib data 
        data = request.get_json()
        temp = data.get('temperature')
        vib = data.get('vibration')

        if temp is None or vib is None:
            return jsonify({"error": " missing 'temp' or 'vib' request data"}), 400
        # 400 means it was a bad request

        prediction = model.predict([[temp, vib]])[0]
        return jsonify({"failure_risk": int(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    # 500 means unexpected error/condition occured

if __name__ == '__main__':
    app.run(debug=True)
