import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Sample dataset (replace with real crop_data.csv if available)
data = {
    "N": [90, 85, 60, 70, 95],
    "P": [40, 35, 20, 25, 42],
    "K": [40, 60, 20, 25, 40],
    "temperature": [20, 25, 30, 22, 28],
    "humidity": [80, 82, 60, 65, 75],
    "ph": [6.5, 7.0, 6.2, 6.8, 7.1],
    "rainfall": [200, 220, 100, 150, 250],
    "label": ["rice", "wheat", "mungbean", "maize", "cotton"]
}

df = pd.DataFrame(data)

X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save trained model
with open("model/crop_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model/crop_model.pkl")
