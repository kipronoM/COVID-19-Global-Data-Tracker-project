import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime

# Set up the visualization style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("Set2")
plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['font.size'] = 12

# Load the OWID COVID-19 data
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

# Display basic information about the dataset
print(f"Dataset shape: {df.shape}")
print("\nFirst 5 rows:")
display(df.head())

print("\nColumns in the dataset:")
print(df.columns.tolist())

print("\nMissing values per column:")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Extract year and month for time-based analysis
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

print("\nTime range in the dataset:")
print(f"From: {df['date'].min()}")
print(f"To: {df['date'].max()}")

print("\nNumber of countries/regions in the dataset:")
print(df['location'].nunique())
