import re
import pandas as pd
import numpy as np

# Extract features from a single URL (used for predictions)
def extract_features(url: str) -> dict:
    return {
        "url_length": len(url),
        "n_dots": url.count('.'),
        "n_hyphens": url.count('-'),
        "n_underline": url.count('_'),
        "n_slash": url.count('/'),
        "n_questionmark": url.count('?'),
        "n_equal": url.count('='),
        "n_at": url.count('@'),
        "n_and": url.count('&'),
        "n_exclamation": url.count('!'),
        "n_space": url.count(' '),
        "n_tilde": url.count('~'),
        "n_comma": url.count(','),
        "n_plus": url.count('+'),
        "n_asterisk": url.count('*'),
        "n_hastag": url.count('#'),
        "n_dollar": url.count('$'),
        "n_percent": url.count('%'),
        "n_redirection": len(re.findall(r'(?<!:)//', url))  # ✅ Improved redirection count
        # Removed: "has_https"
    }

# Extract features from a DataFrame column (used for training)
def extract_features_from_dataframe(df, url_column="url"):
    features = df[url_column].apply(extract_features)
    return features.apply(pd.Series)

# Extract features from a single URL and return as numpy array
def extract_features_single(url: str):
    features = extract_features(url)
    return np.array(list(features.values()))
