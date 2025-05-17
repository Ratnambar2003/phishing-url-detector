# 🛡️ Phishing URL Detector using XGBoost and Flask

This project is a **machine learning-based web application** that predicts whether a given URL is **phishing** or **legitimate**. It uses the **XGBoost classifier** and the **Flask web framework** to provide real-time prediction through a simple browser interface.

---

## 🚀 Features

- 🔍 Detects phishing URLs using 19 numerical features
- 🧠 Model trained with XGBoost (Extreme Gradient Boosting)
- 💾 Model saved using `joblib` for fast loading
- 🌐 Clean and simple web interface powered by Flask
- 📦 Well-structured project — easy to extend and modify

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
├── assets/ # Images used (optional for frontend or docs)
│ ├── 122.png
│ ├── 6049722.png
│ └── 9635979.png
│
├── data/
│ └── phishing1.csv # Dataset with URL features and labels
│
├── models/
│ └── phishing_xgb_model.pkl # Trained XGBoost model saved with joblib
│
├── scripts/ # (Currently empty or for future utilities)
│
├── src/ # Source code for model & feature processing
│ ├── init.py
│ ├── feature_extraction.py # Script to extract 19 features from a URL
│ └── model.py # Model training logic
│
├── templates/
│ └── index.html # HTML page served by Flask
│
├── app.py # Main Flask app for frontend/backend
├── data.py # Data handling (optional usage)
├── feature.py # Possibly URL feature handling
├── main.py # Could be entry point or testing script
└── README.md # Project documentation



---

## 🏃‍♂️ How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt


Run the Flask app:

bash
python app.py


Open your browser and visit:
http://127.0.0.1:5000/

📊 Model Details
Algorithm: XGBoost Classifier

Training Data: Extracted features from URLs stored in phishing1.csv

Features: 19 numerical values derived from each URL

Labels: 0 = Legitimate, 1 = Phishing

Model Storage: joblib (phishing_xgb_model.pkl)

📬 Developed By
RATNAMBAR BAGHEL, SHARARAT ALAM
Minor Project Submission - B.Tech
Department of Computer Science (AIML)
Rungta College of Engineering and Technology
Email: [6604663@rungta.org]

🔍 Feature Insights Used in Prediction
Our model uses 19 handcrafted features extracted from each URL to classify it as phishing or legitimate. Below are some key features:

| Feature Name               | Description                            | Typical in Phishing? | Legitimate Example                                     | Phishing Example                                                                                                           |
| -------------------------- | -------------------------------------- | -------------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| URL\_Length                | Total number of characters in URL      | Yes (long)           | [https://www.amazon.com](https://www.amazon.com)       | [http://verify-your-amazon-account.com/login/security/update](http://verify-your-amazon-account.com/login/security/update) |
| Having\_At\_Symbol         | Presence of `@` symbol in URL          | Yes                  | [https://gmail.com](https://gmail.com)                 | [http://example.com@phishingsite.com](http://example.com@phishingsite.com)                                                 |
| Prefix\_Suffix             | Use of hyphen (`-`) in domain name     | Yes                  | [https://paypal.com](https://paypal.com)               | [http://secure-paypal-login.com](http://secure-paypal-login.com)                                                           |
| DNS\_Record                | Whether DNS record exists              | No (missing)         | Yes (exists)                                           | No (non-existent)                                                                                                          |
| HTTPS\_Token               | Misuse of "https" in URL (fake https)  | Yes                  | [https://secure.bank.com](https://secure.bank.com)     | [http://https-secure-bank.com](http://https-secure-bank.com)                                                               |
| Having\_IP\_Address        | IP address used instead of domain name | Yes                  | [https://www.google.com](https://www.google.com)       | [http://192.168.1.1/login](http://192.168.1.1/login)                                                                       |
| Double\_Slash\_Redirecting | Redirect after `//` in URL             | Yes                  | [https://linkedin.com](https://linkedin.com)           | [http://site.com//malicious-site.com](http://site.com//malicious-site.com)                                                 |
| Abnormal\_URL              | Unusual domain name or mismatch        | Yes                  | [https://www.icicibank.com](https://www.icicibank.com) | [http://icici.bank.login.verify.ru](http://icici.bank.login.verify.ru)                                                     |
| TinyURL                    | Use of URL shortener                   | Yes                  | [https://netflix.com](https://netflix.com)             | [https://bit.ly/3xYz1](https://bit.ly/3xYz1)                                                                               |
| Domain\_Age                | Domain age (new = risky)               | New = Risk           | >1 year                                                | <1 month                                                                                                                   |

⚠️ Example URLs
Phishing example: http://faceb00k-login-security.xyz/

Legitimate example: https://www.facebook.com/
