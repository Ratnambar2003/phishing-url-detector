import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from xgboost import XGBClassifier
import joblib

def train_model(data_path="data/phishing1.csv", save_model=True):
    # Load preprocessed dataset (already has features and label)
    df = pd.read_csv(data_path)

    # Features & label
    X = df.drop(columns=["phishing"])
    y = df["phishing"]

    print("Training on features:", X.columns.tolist())

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print("Classification Report:\n", classification_report(y_test, y_pred))
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")

    # Save model
    if save_model:
        os.makedirs("models", exist_ok=True)
        model_path = os.path.abspath("models/phishing_xgb_model.pkl")
        try:
            joblib.dump(model, model_path)
            print(f"[OK] Model saved to {model_path}")
        except Exception as e:
            print(f"[ERROR] Failed to save model: {e}")

    return model
