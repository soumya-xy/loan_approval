from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model
try:
    model = pickle.load(open('model/loan_model.pkl', 'rb'))
except Exception as e:
    print("Error loading model:", e)
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return "Model not loaded", 500

    try:
        # Collect form inputs
        data = {
            ' no_of_dependents': float(request.form['dependents']),
            ' education': 1 if request.form['education'] == 'Graduate' else 0,
            ' self_employed': 1 if request.form['self_employed'] == 'Yes' else 0,
            ' income_annum': float(request.form['income']),
            ' loan_amount': float(request.form['loan_amount']),
            ' loan_term': float(request.form['loan_term']),
            ' cibil_score': float(request.form['cibil_score']),
            ' residential_assets_value': float(request.form['residential_assets']),
            ' commercial_assets_value': float(request.form['commercial_assets']),
            ' luxury_assets_value': float(request.form['luxury_assets']),
            ' bank_asset_value': float(request.form['bank_assets'])
        }

        # Derived features
        movable_assets = data[' bank_asset_value'] + data[' luxury_assets_value']
        immovable_assets = data[' residential_assets_value'] + data[' commercial_assets_value']

        # Ensure feature names match the trained model (with spaces)
        input_data = pd.DataFrame([[
            data[' no_of_dependents'],
            data[' education'],
            data[' self_employed'],
            data[' income_annum'],
            data[' loan_amount'],
            data[' loan_term'],
            data[' cibil_score'],
            movable_assets,
            immovable_assets
        ]], columns=[
            ' no_of_dependents',
            ' education',
            ' self_employed',
            ' income_annum',
            ' loan_amount',
            ' loan_term',
            ' cibil_score',
            'Movable_assets',
            'Immovable_assets'
        ])

        # Prediction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        result = {
            'prediction': "Approved" if prediction == 1 else "Not Approved",
            'probability': f"{probability*100:.2f}%",
            'input_data': data
        }

        return render_template('result.html', result=result)

    except Exception as e:
        return f"An error occurred: {str(e)}", 400

if __name__ == '__main__':
    app.run(debug=True)
