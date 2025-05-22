from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

# Load your model
with open('notebooks/titanic_model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)
# Manual mappings (must match training phase)
sex_map = {'male': 0, 'female': 1}
title_map = {'Mr': 0, 'Miss': 1, 'Mrs': 2, 'Master': 3}
embarked_map = {'C': 0, 'Q': 1, 'S': 2}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input
        Pclass = int(request.form['Pclass'])
        Sex = sex_map[request.form['Sex']]
        Age = float(request.form['Age'])
        SibSp = int(request.form['SibSp'])
        Parch = int(request.form['Parch'])
        Fare = float(request.form['Fare'])
        Embarked = embarked_map[request.form['Embarked']]
        Title = title_map[request.form['Title']]

        # Derived features
        FamilySize = SibSp + Parch
        IsAlone = 1 if FamilySize == 0 else 0

        # Final input
        final_input = np.array([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked, Title, FamilySize, IsAlone]])

        # Prediction
        prediction = model.predict(final_input)[0]

        result = "Survived 😊" if prediction == 1 else "Did Not Survive 😢"
        return render_template('result.html', prediction=result)

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
