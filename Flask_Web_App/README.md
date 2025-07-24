# 🚢 Titanic Survival Prediction - Flask Web App

This is a Flask-based web application that predicts whether a Titanic passenger would have survived or not based on their personal and travel information. It uses a pre-trained Random Forest model wrapped in a scikit-learn pipeline, with custom feature engineering.


---

## 🔍 Project Features

- 🔄 **Machine Learning Pipeline** with preprocessing and classification
- 🧠 **Feature Engineering**: Title extraction, FamilySize, IsAlone
- 🧾 **User Input Form** for passenger details
- 📊 **Probability-based prediction** using `RandomForestClassifier`
- 🎨 **Stylish and responsive interface** with HTML/CSS
- 💻 **Deployed-ready structure** (can be hosted on Railway, Render, Heroku, etc.)

---

## 🚀 How to Run the App Locally

### 1. Clone the Repository

```
git clone https://github.com/yourusername/titanic-flask-app.git
cd titanic-flask-app
```
### 2. Create and Activate a Virtual Environment
### Windows
```
python -m venv venv
venv\Scripts\activate
```
### macOS/Linux
```
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
Make sure you have Python 3.7 or higher installed.
### 4. Run the Flask App
```
python app.py
```
Then open your browser and go to: http://127.0.0.1:5000
## Model & Pipeline
The model was trained on the Titanic dataset using:

RandomForestClassifier

OneHotEncoder for categorical features

Custom engineered features:

Title (from passenger name)

FamilySize (SibSp + Parch + 1)

IsAlone (1 if traveling alone)

The final pipeline was saved using joblib:

joblib.dump(pipeline, 'titanic_pipeline.joblib')
## 📁 Folder Structure
```
titanic-flask-app/
│
├── app.py
├── titanic_pipeline.joblib
├── requirements.txt
├── templates/
│   ├── index.html
│   └── result.html
└── README.md
```
🔘 Input Form (index.html):


✅ Prediction Result (result.html):


</details>
📦 Deployment
This app can be deployed to any Python-compatible hosting service like:

Railway

Render

Heroku

Replit

Let us know if you need a Dockerfile, Procfile, or deployment tutorial.

🙋‍♀️ Author
Built by Durdana Khalid

📄 License
This project is open-source and available under the MIT License.
