# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("healthcare_noshows.csv")

# Basic info
print("Shape:", df.shape)
print("\nColumns:", df.columns)
print("\nMissing values:\n", df.isnull().sum())

# Target column analysis
print("\nShow-up counts:\n", df['Showed_up'].value_counts())
print("\nShow-up %:\n", df['Showed_up'].value_counts(normalize=True) * 100)

# Gender vs No-show
gender_noshow = df.groupby('Gender')['Showed_up'].value_counts(normalize=True) * 100
print("\nNo-show % by Gender:\n", gender_noshow)

# SMS vs No-show
sms_noshow = df.groupby('SMS_received')['Showed_up'].value_counts(normalize=True) * 100
print("\nNo-show % with/without SMS:\n", sms_noshow)

# Average age
print("\nAverage Age of Patients:", df['Age'].mean())

# --- Visualizations ---
# Gender vs No-show
sns.countplot(x="Gender", hue="Showed_up", data=df)
plt.title("Show-up by Gender")
plt.show()

# SMS Reminder vs No-show
sns.countplot(x="SMS_received", hue="Showed_up", data=df)
plt.title("Effect of SMS Reminder on Show-up")
plt.show()

# Age Distribution
plt.figure(figsize=(8,4))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Age Distribution of Patients")
plt.show()
