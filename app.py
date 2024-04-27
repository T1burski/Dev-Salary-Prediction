import pickle
from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Loading our previously trained model
model = pickle.load(open('artifacts/model_regressor.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
         data = {
            'Country': request.form['Country'],
            'DevType' : request.form['devtype'],
            'EdLevel': request.form['education'],
            'YearsCodePro': float(request.form['experience']),
                }
    except ValueError as e:
        return render_template("home.html", prediction_text=f"Invalid Entry. Error: {e}")

    if any(value == '' for value in data.values()):
        return render_template("home.html", prediction_text="Verify if all fileds are filled.")
    
    # using the model to predict the inputs made by the user
    output = model.predict(pd.DataFrame([data]))[0]

    formatted_output = round(output, 2)
    
    return render_template("home.html", prediction_text="The estimated salary is $ {} [yearly]".format(formatted_output))

if __name__ == "__main__":
    app.run()














