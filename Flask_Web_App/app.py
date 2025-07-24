from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained pipeline
model = joblib.load("model/titanic_pipeline.joblib")

# --------------- Feature Engineering Function ---------------
def add_custom_features(df):
    df = df.copy()

    # Extract Title from Name
    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    df['Title'] = df['Title'].replace(['Lady', 'Countess', 'Capt', 'Col', 'Don',
                                       'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    df['Title'] = df['Title'].replace(['Mlle', 'Ms'], 'Miss')
    df['Title'] = df['Title'].replace('Mme', 'Mrs')
    df['Title'] = df['Title'].fillna("Unknown")

    # Create FamilySize and IsAlone
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

    # Ensure strings for categorical features
    for col in ['Sex', 'Embarked', 'Title']:
        df[col] = df[col].astype(str).fillna("Missing")

    return df


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect form inputs
        input_dict = {
            "Pclass": int(request.form["pclass"]),
            "Sex": request.form["sex"],
            "Age": float(request.form["age"]),
            "SibSp": int(request.form["sibsp"]),
            "Parch": int(request.form["parch"]),
            "Fare": float(request.form["fare"]),
            "Embarked": request.form["embarked"],
            "Name": request.form["name"]
        }

        # Create dataframe and add features
        df = pd.DataFrame([input_dict])
        df = add_custom_features(df)

        # Select only model input columns
        input_data = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare',
                         'Embarked', 'Title', 'FamilySize', 'IsAlone']]

        # Predict
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        result = "Survived 🟢" if prediction == 1 else "Did Not Survive 🔴"
        return render_template("result.html",
                               result=result,
                               probability=f"{probability * 100:.2f}%")

    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
