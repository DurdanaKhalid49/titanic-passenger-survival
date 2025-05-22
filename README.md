# 🚢 Titanic Passenger Survival Prediction App

This project uses the Titanic dataset to predict whether a passenger survived, based on features like age, gender, passenger class, and family information. It includes:

- 🎯 A **Flask web app** to make predictions
- 📊 A **Plotly Dash dashboard** to explore survival trends
- 📈 A **Power BI dashboard** (coming soon)

---

## 📁 Project Structure

├── app.py # Flask app
├── model.pkl # Trained Random Forest model
├── cleaned_data.csv # Final dataset
├── Dash_App/ # Interactive Dash app
├── templates/ # HTML templates (index, result)
├── requirements.txt
├── Procfile # Deployment file (for Render/Heroku)
└── README.md

yaml
Copy
Edit

---

## 🧠 Features

### 🔍 Flask App:
- Inputs: Age, Sex, Pclass, Fare, etc.
- Output: Survival prediction using a trained RandomForestClassifier

### 📊 Dash App:
- Filters: Sex, Embarked
- KPIs: Average age, survival rate
- Graphs: Interactive bar/pie charts using Plotly

---

## 🚀 Installation

```bash
git clone https://github.com/yourusername/Titanic-Passenger-Survival.git
cd Titanic-Passenger-Survival
pip install -r requirements.txt
Run Flask app:
bash
Copy
Edit
python app.py
Run Dash app:
bash
Copy
Edit
cd Dash_App
python app.py
📦 Requirements
See requirements.txt for full dependencies.

📊 Power BI Dashboard
Power BI dashboard will be added soon to visualize:

Survival rate by class and gender

Average fare by port of embarkation

Slicers and interactive visuals

🔗 Live Demo
🚀 Deployed version coming soon via Render!

💼 Author
Durdana Khalid
Aspiring Data Scientist | Skilled in Python, ML, Dash, Power BI
https://www.linkedin.com/in/durdana-khalid-66b6461ba/ | Portfolio Coming Soon

📄 License
This project is open-source and free to use.
