import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import pickle

# Load your dataset
df = pd.read_csv("your_cleaned_titanic.csv")

# Define features and target
X = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_Q', 'Embarked_S', 'Title', 'FamilySize', 'IsAlone']]
y = df['Survived']

# Categorical columns to one-hot encode
categorical_cols = ['Sex', 'Title']
# 'Embarked_Q' and 'Embarked_S' are already binary columns

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ],
    remainder='passthrough'  # keep other columns as-is
)

# Full pipeline
clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
clf.fit(X_train, y_train)

# Save the full pipeline
with open('titanic_pipeline.pkl', 'wb') as f:
    pickle.dump(clf, f)
