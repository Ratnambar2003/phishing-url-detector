import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
data=pd.read_csv("data/phishing1.csv")

#data cleaning 

print(data)
print(data.head())
print(data.isnull().sum())
print(data.describe())
data.drop_duplicates(inplace=True)

#Data visualization
#Histogram(URL Length Distribution)

plt.hist(data['url_length'],bins=60,edgecolor='Black',color='Blue',alpha=0.7)
plt.xlabel("URL Length")
plt.ylabel('Frequency')
plt.title("Distribution of URL Lengths")
plt.show()

#Bar Chart(Phishing vs Legitimate URLs)

data['phishing'].value_counts().plot(kind='bar',color=['green','red'])
plt.xlabel('Class (0=Legitimate, 1=Phishing)')
plt.ylabel('Counts')
plt.title("Phishing vs. Legitimate URLs")
plt.show()

#Pie chart (phishing Proportion)

data['phishing'].value_counts().plot(kind='pie',autopct='%1.1f%%',colors=['green','red'])
plt.title("Proportion of Phishing URLs")
plt.ylabel('')
plt.show()

#Heatmap (Feature Correlation)

plt.figure(figsize=(12,8))
sns.heatmap(data.corr(),annot=True,cmap='coolwarm',linewidths=0.5)
plt.title('Feature Correlation Heatmap')
plt.show()


#Export data in MySQL

#Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Baghel04",
    database="phishing_db"
)
cursor = conn.cursor()

# Insert data into MySQL
for _, row in data.iterrows():
    sql = """
    INSERT INTO phishing_data (url_length, n_dots, n_hypens, n_underline, n_slash, n_questionmark,
                               n_equal, n_at, n_and, n_exclamation, n_space, n_tilde, n_comma, n_plus,
                               n_asterisk, n_hastag, n_dollar, n_percent, n_redirection, phishing)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, tuple(row))

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

print("Data exported to MySQL successfully!")