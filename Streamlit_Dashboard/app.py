import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("model/titanic_pipeline.joblib")

# Streamlit page setup
st.set_page_config(page_title="🚢 Titanic Survival Prediction", layout="wide", page_icon="🧊")

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #f9f9f9; }
    h1, h2, h3 { color: #004d99; }
    .stButton>button {
        background-color: #004d99;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .stButton>button:hover { background-color: #0066cc; }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🧊 Titanic Passenger Survival Dashboard")
st.markdown("Predict whether a passenger would have survived the Titanic disaster using machine learning!")

# Sidebar - input method
st.sidebar.header("🔧 Select Input Mode")
mode = st.sidebar.radio("Choose input method:", ["Upload CSV", "Manual Input"])

def add_custom_features(df):
    df = df.copy()

    # Title extraction from Name
    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    df['Title'] = df['Title'].replace(['Lady', 'Countess', 'Capt', 'Col', 'Don',
                                       'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    df['Title'] = df['Title'].replace(['Mlle', 'Ms'], 'Miss')
    df['Title'] = df['Title'].replace('Mme', 'Mrs')

    # Fill missing titles
    df['Title'] = df['Title'].fillna("Unknown")

    # FamilySize
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

    # IsAlone
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

    # Safety: ensure all categorical columns are strings
    for col in ['Sex', 'Embarked', 'Title']:
        df[col] = df[col].astype(str)
        df[col] = df[col].fillna("Missing")  # If somehow null sneaks in

    return df


# ---- Prediction function ----
def make_prediction(input_df):
    prediction = model.predict(input_df)
    prob = model.predict_proba(input_df)
    return prediction, prob

# ---- CSV Upload ----
if mode == "Upload CSV":
    st.subheader("📂 Upload Passenger Data CSV")
    uploaded_file = st.file_uploader("Upload your Titanic passenger CSV", type=["csv"])

    if uploaded_file:
        data = pd.read_csv(uploaded_file)

        required_columns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Name']
        if not set(required_columns).issubset(data.columns):
            st.error(f"❌ Your file must contain the following columns: {required_columns}")
        else:
            data = add_custom_features(data)
            input_data = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Title', 'FamilySize', 'IsAlone']]
            
            if st.button("Predict Survival"):
                prediction, prob = make_prediction(input_data)
                data['Prediction'] = np.where(prediction == 1, 'Survived', 'Did Not Survive')
                data['Survival Probability (%)'] = (prob[:, 1] * 100).round(2)
                st.success("✅ Prediction complete!")
                st.write("### Result", data[['Name', 'Prediction', 'Survival Probability (%)']])
                st.download_button("Download Results as CSV", data.to_csv(index=False), file_name="titanic_predictions.csv")

# ---- Manual Input ----
else:
    st.subheader("✍️ Enter Passenger Details")

    col1, col2, col3 = st.columns(3)
    with col1:
        Pclass = st.selectbox("Ticket Class (Pclass)", [1, 2, 3])
        Sex = st.selectbox("Sex", ["male", "female"])
        Embarked = st.selectbox("Port of Embarkation", ["S", "C", "Q"])

    with col2:
        Age = st.number_input("Age", min_value=0.42, max_value=80.0, value=30.0)
        SibSp = st.number_input("Siblings/Spouses Aboard", 0, 10, value=0)
        Parch = st.number_input("Parents/Children Aboard", 0, 10, value=0)

    with col3:
        Fare = st.number_input("Fare", min_value=0.0, value=32.20, step=0.1)
        Name = st.text_input("Passenger Name", "Mr. John Doe")

    # Create a single-row DataFrame
    raw_input = pd.DataFrame([{
        "Pclass": Pclass,
        "Sex": Sex,
        "Age": Age,
        "SibSp": SibSp,
        "Parch": Parch,
        "Fare": Fare,
        "Embarked": Embarked,
        "Name": Name
    }])

    processed_input = add_custom_features(raw_input)
    input_df = processed_input[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked', 'Title', 'FamilySize', 'IsAlone']]

    if st.button("Predict Survival"):
        prediction, prob = make_prediction(input_df)
        result = " Survived" if prediction[0] == 1 else " Did Not Survive"
        color = "#2ecc71" if prediction[0] == 1 else "#e74c3c"
        st.markdown(f"<h2 style='color:{color}'>Prediction: {result}</h2>", unsafe_allow_html=True)
        st.markdown(f"**Survival Probability:** {prob[0][1]*100:.2f}%")

# ---- Footer ----
st.markdown("---")
st.markdown("🚀 Built by [Durdana Khalid](https://github.com/DurdanaKhalid49)")
