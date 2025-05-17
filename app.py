import os
import sys
import pandas as pd
from flask import Flask, render_template, request, jsonify, send_from_directory
from urllib.parse import urlparse
import re
import joblib

# 👉 Add the path so Python can find src/feature_extraction.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from feature_extraction import extract_features

# Load trained model
model = joblib.load('models/phishing_xgb_model.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Serve CSS & JS from /scripts/
@app.route('/scripts/<path:filename>')
def serve_scripts(filename):
    return send_from_directory('scripts', filename)

# Serve image from /assets/
@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('assets', filename)

@app.route('/check', methods=['POST'])
def check_url():
    data = request.get_json()
    input_url = data.get('url')

    if not input_url:
        return jsonify({'safe': False, 'message': 'Please enter a URL'})

    try:
        url = urlparse(input_url)
    except Exception:
        return jsonify({'safe': False, 'message': 'Invalid URL format'})

    # ✅ Extended Trusted Domains Check
    trusted_domains = [
        # Tech Giants
        'google.com', 'gmail.com', 'youtube.com', 'googleusercontent.com',
        'microsoft.com', 'live.com', 'outlook.com', 'msn.com',
        'apple.com', 'icloud.com',

        # Social Media
        'facebook.com', 'instagram.com', 'twitter.com', 'linkedin.com',
        'snapchat.com', 'tiktok.com', 'pinterest.com',

        # Messaging Platforms
        'whatsapp.com', 'chat.whatsapp.com', 'wa.me', 'telegram.org',
        'discord.com', 'slack.com',

        # E-commerce
        'amazon.com', 'flipkart.com', 'ebay.com', 'aliexpress.com',

        # Payment & Banking
        'paypal.com', 'stripe.com', 'paytm.com', 'phonepe.com',
        'googlepay.com', 'razorpay.com',

        # Government & Education
        'gov.in', 'gov.uk', 'edu.in', 'edu.com',

        # Cloud & Dev Platforms
        'github.com', 'gitlab.com', 'bitbucket.org',
        'vercel.app', 'netlify.app', 'firebaseapp.com', 'herokuapp.com',
        'pythonanywhere.com',

        # OpenAI & AI
        'openai.com', 'chat.openai.com', 'platform.openai.com', 'api.openai.com',
        'chatgpt.com', 'huggingface.co',

        # Your Own Domain
        'ratnambar.pythonanywhere.com'
    ]

    domain = url.netloc.lower()
    if domain.startswith('www.'):
        domain = domain[4:]

    if any(td in domain for td in trusted_domains):
        return jsonify({'safe': True, 'message': '✅ Trusted website. This URL is safe.'})

    # ✨ Machine Learning Prediction
    try:
        features = extract_features(input_url)
        feature_order = [
            'url_length', 'n_dots', 'n_hyphens', 'n_underline', 'n_slash', 'n_questionmark',
            'n_equal', 'n_at', 'n_and', 'n_exclamation', 'n_space', 'n_tilde', 'n_comma',
            'n_plus', 'n_asterisk', 'n_hastag', 'n_dollar', 'n_percent', 'n_redirection'
        ]
        feature_df = pd.DataFrame([[features[col] for col in feature_order]], columns=feature_order)
        prediction = model.predict(feature_df)[0]

        if prediction == 0:
            return jsonify({'safe': True, 'message': '✅ This URL is likely safe.'})
        else:
            return jsonify({'safe': False, 'message': '🚨 This URL is likely a phishing site.'})

    except Exception as e:
        return jsonify({'safe': False, 'message': f'Model error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)
