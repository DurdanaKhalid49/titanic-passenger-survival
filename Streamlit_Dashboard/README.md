# 🧊 Titanic Passenger Survival – Streamlit Dashboard

This is a **Streamlit web app** that predicts whether a passenger would have survived the Titanic disaster based on input features like class, age, gender, fare, and more. The model is trained using scikit-learn and deployed with a clean, user-friendly interface.

## 🚀 Live Demo

🔗 [Click here to open the live dashboard](https://your-app-url.streamlit.app)

---

## 📌 Project Features

- 🌐 Web interface built using **Streamlit**
- 🤖 Predicts **Survival vs Non-survival** using a trained ML model
- 📥 Accepts **CSV upload** or **manual input**
- 📊 Shows survival **probability percentage**
- 🧼 Clean layout with a modern UI

---

## 🧠 Model Details

- ✅ Preprocessing handled via pipeline (OneHotEncoding, Imputation, etc.)
- 🎯 Final model: `RandomForestClassifier` or `XGBoostClassifier` (as per training)
- 🔁 Compatible with batch prediction (multiple passengers via CSV)

---

## 📂 Folder Structure

Titanic_Passenger_Survival_Streamlit_Dashboard/
│
├── app.py # Streamlit app code
├── model/
│ └── titanic_pipeline_model.joblib # Trained model pipeline
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🛠️ Installation & Running Locally

### ✅ Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/Titanic_Passenger_Survival_Streamlit_Dashboard.git
cd Titanic_Passenger_Survival_Streamlit_Dashboard
✅ Step 2: Create virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate       # On Windows
source venv/bin/activate   # On Mac/Linux
✅ Step 3: Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
✅ Step 4: Run the app
bash
Copy
Edit
streamlit run app.py
📈 Input Features
Feature	Description
Pclass	Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)
Sex	Gender of passenger
Age	Age in years
SibSp	# of siblings/spouses aboard
Parch	# of parents/children aboard
Fare	Ticket fare paid
Embarked	Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)
Cabin	Cabin code (optional, can be empty)

📸 Screenshots
Manual Input Prediction	Batch CSV Prediction

🧑‍💻 Author
Durdana Khalid
🔗 GitHub
📬 Feel free to connect for collaboration or feedback!

📜 License
This project is licensed under the MIT License.