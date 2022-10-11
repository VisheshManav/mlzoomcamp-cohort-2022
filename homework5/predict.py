import pickle
from flask import Flask
from flask import request
from flask import jsonify

input_dv = './dv.bin'
input_model = './model2.bin'

with open(input_dv, 'rb') as f_dv, \
        open(input_model, 'rb') as f_model:
    dv = pickle.load(f_dv)
    model = pickle.load(f_model)

app = Flask('credit')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]

    result = {
        'credit_card_getting_prob': float(y_pred)
    }
    return jsonify(result)

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=9696)
