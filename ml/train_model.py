import json
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
import os

# Load dataset
with open('backend/dataset.json', 'r') as f:
    data = json.load(f)

print(f"Loaded {len(data)} training samples")

# Extract features and labels
interests = [entry['interest'] for entry in data]
experiences = [entry['experience'] for entry in data]
personalities = [entry['personality'] for entry in data]
skills_list = [entry['skills'] for entry in data]
jobs = [entry['job'] for entry in data]

# Create MultiLabelBinarizer for skills
mlb = MultiLabelBinarizer()
skills_encoded = mlb.fit_transform(skills_list)

# Create encoders for categorical features
interest_encoder = LabelEncoder()
interest_encoded = interest_encoder.fit_transform(interests)

experience_encoder = LabelEncoder()
experience_encoded = experience_encoder.fit_transform(experiences)

personality_encoder = LabelEncoder()
personality_encoded = personality_encoder.fit_transform(personalities)

# Job encoder
job_encoder = LabelEncoder()
job_encoded = job_encoder.fit_transform(jobs)

# Combine all features
X = np.hstack([
    interest_encoded.reshape(-1, 1),
    experience_encoded.reshape(-1, 1),
    personality_encoded.reshape(-1, 1),
    skills_encoded
])

y = job_encoded

# Train Decision Tree model
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X, y)

print(f"Model trained successfully!")
print(f"Feature count: {X.shape[1]}")
print(f"Classes: {len(job_encoder.classes_)}")

# Save model and encoders
os.makedirs('backend', exist_ok=True)

model_data = {
    'model': model,
    'interest_encoder': interest_encoder,
    'experience_encoder': experience_encoder,
    'personality_encoder': personality_encoder,
    'job_encoder': job_encoder,
    'mlb': mlb,
    'job_list': job_encoder.classes_
}

with open('backend/model.pkl', 'wb') as f:
    pickle.dump(model_data, f)

print("Model saved to backend/model.pkl")
