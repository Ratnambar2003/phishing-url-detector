# 🛡️ Phishing URL Detector using XGBoost and Flask

This project is a **machine learning-based web application** that predicts whether a given URL is **phishing** or **legitimate**. It is built using the **XGBoost classifier** and a **Flask web framework** for real-time prediction through a simple browser-based interface.

---

## 🚀 Features

- 🔍 Detects phishing URLs using 19 numerical features
- 🧠 Model trained using XGBoost (Extreme Gradient Boosting)
- 💾 Model saved using `joblib` for faster loading
- 🌐 Clean and simple web interface using Flask
- 📦 Structured project — easy to modify or expand

---

## 🧰 Tech Stack

- Python 3.x
- Flask
- XGBoost
- Joblib
- Pandas
- NumPy
- Scikit-learn

---

## 📁 Project Structure

URL_DETECTOR_ML/
│
├── assets/                         # Images used (optional for frontend or docs)
│   ├── 122.png
│   ├── 6049722.png
│   └── 9635979.png
│
├── data/
│   └── phishing1.csv              # Dataset containing URL features and labels
│
├── models/
│   └── phishing_xgb_model.pkl     # Trained XGBoost model saved with joblib
│
├── scripts/                       # (Currently empty or for future utilities)
│
├── src/                           # Source code for model & feature processing
│   ├── __init__.py
│   ├── feature_extraction.py      # Script to extract 19 features from a URL
│   └── model.py                   # Model training logic
│
├── templates/
│   └── index.html                 # HTML page served via Flask
│
├── app.py                         # Main Flask app for frontend/backend
├── data.py                        # Data handling (optional usage)
├── feature.py                     # Possibly URL feature handling
├── main.py                        # Could be entry point or testing script
└── README.md                      # Project documentation

Run the app

bash
Copy
Edit
python app.py
Visit in your browser

cpp
Copy
Edit
http://127.0.0.1:5000/

📊 Model Details
Algorithm: XGBoost Classifier

Training data: Extracted features from URLs stored in phishing1.csv

Features: 19 numerical values derived from each URL

Labels: 0 = Legitimate, 1 = Phishing

Model Storage: joblib (phishing_xgb_model.pkl)

📬 Developed By
RATNAMBAR BAGHEL,SHARARAT ALAM
Minor Project Submission - B.Tech 
Department of Computer Science (AIML)
Rungta college of engineering and technology
Email: [6604663@rungta.org]



phisng url-http://faceb00k-login-security.xyz/

legitimate url-https://www.facebook.com/



## 🔍 Feature Insights Used in Prediction

Our model uses 19 handcrafted features extracted from each URL to determine whether it is **phishing** or **legitimate**. Below are some key features:

| 🔢 Feature Name             | 📖 Description                                                                 | 🧪 Typical in Phishing? | ✅ Legitimate Example              | 🚨 Phishing Example                    |
|----------------------------|----------------------------------------------------------------------------------|--------------------------|------------------------------------|----------------------------------------|
| `URL_Length`               | URL ka total length (characters)                                                | Yes (long)               | https://www.amazon.com             | http://verify-your-amazon-account.com/login/security/update |
| `Having_At_Symbol`         | URL me `@` symbol ka hona                                                       | Yes                      | https://gmail.com                  | http://example.com@phishingsite.com    |
| `Prefix_Suffix`            | Domain me hyphen (`-`) ka use                                                   | Yes                      | https://paypal.com                 | http://secure-paypal-login.com         |
| `DNS_Record`               | Domain ka DNS record available hai ya nahi                                      | No (missing)             | Yes (exists)                       | No (non-existent)                      |
| `HTTPS_Token`             | "https" word misuse in URL (fake https)                                         | Yes                      | https://secure.bank.com            | http://https-secure-bank.com           |
| `Having_IP_Address`        | Kya domain name me IP address use kiya gaya hai?                                | Yes                      | https://www.google.com             | http://192.168.1.1/login               |
| `Double_Slash_Redirecting`| `//` ke baad redirect URL hai kya?                                              | Yes                      | https://linkedin.com               | http://site.com//malicious-site.com    |
| `Abnormal_URL`             | Kya domain name unusual hai (e.g., mismatch with actual brand)?                 | Yes                      | https://www.icicibank.com          | http://icici.bank.login.verify.ru      |
| `TinyURL`                  | Shortened URL use kiya gaya hai?                                                | Yes                      | https://netflix.com                | https://bit.ly/3xYz1                   |
| `Domain_Age`               | Domain kitna purana hai?                                                        | New = Risk               | >1 year                            | <1 month                               |

