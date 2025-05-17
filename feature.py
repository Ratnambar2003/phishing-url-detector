import pandas as pd
import pymysql

# MySQL connection
conn = pymysql.connect(host='localhost', user='root', password='@Baghel04', db='phishing_db')

# Query to find YouTube URL
query = "SELECT * FROM phishing_data WHERE n_dots > 3"  # ya koi bhi dusra condition
df = pd.read_sql(query, conn)

# Close connection
conn.close()

# Display first matching row
print(df.head(1))

# Extract features (assuming 'url' and 'phishing' are the non-feature columns)
features = df.drop(columns=['phishing']).iloc[0].to_dict()

print(features)
