import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

for dirname, _, filenames in os.walk(r"C:\Users\ccrou\OneDrive\Desktop\saturnDataCSV.csv"):
     for filename in filenames:
       print(os.path.join(dirname, filename))
os.listdir(r"C:\Users\ccrou\OneDrive\Desktop")

path = r"C:\Users\ccrou\OneDrive\Desktop\saturnDataCSV.csv"
data = pd.read_csv(path, encoding='UTF-8')
df = pd.DataFrame(data)
df_clean_p = df.dropna()
print(df_clean_p)

#data with no n/a vals including phoebe
df_clean_p = df.dropna()
print(df_clean_p)

#data cleaned but phoebe removed
df_clean = df_clean_p.drop(40)
print(df_clean)

#VISUALIZATION FOR ALL RINGS

#make sure data is numeric and plot for data including Phoebe
df_clean_p['Inner Boundary (km)'] = pd.to_numeric(df_clean_p['Inner Boundary (km)'].replace({',': ''}, regex=True), errors='coerce')
df_clean_p['Outer Boundary (km)'] = pd.to_numeric(df_clean_p['Outer Boundary (km)'].replace({',': ''}, regex=True), errors='coerce')

plt.figure(figsize=(14, 8))

# Plot inner boundaries
sns.barplot(x='Feature', y='Inner Boundary (km)', data=df_clean_p, color='blue', label='Inner Boundary')
# Plot outer boundaries on top of inner boundaries
sns.barplot(x='Feature', y='Outer Boundary (km)', data=df_clean_p, color='orange', label='Outer Boundary', bottom=df_clean_p['Inner Boundary (km)'])

plt.xticks(rotation=90)
plt.xlabel('Feature')
plt.ylabel('Distance from Saturn (km)')
plt.title('Feature Boundaries in Relation to Distance from Saturn')
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()

#VISUALIZATION FOR RINGS EXCLUDING PHOEBE RING

#make sure data is numeric and plot for data EXCLUDING Phoebe
df_clean['Inner Boundary (km)'] = pd.to_numeric(df_clean['Inner Boundary (km)'].replace({',': ''}, regex=True), errors='coerce')
df_clean['Outer Boundary (km)'] = pd.to_numeric(df_clean['Outer Boundary (km)'].replace({',': ''}, regex=True), errors='coerce')

plt.figure(figsize=(14, 8))

# Plot inner boundaries
sns.barplot(x='Feature', y='Inner Boundary (km)', data=df_clean, color='blue', label='Inner Boundary')
# Plot outer boundaries on top of inner boundaries
sns.barplot(x='Feature', y='Outer Boundary (km)', data=df_clean, color='orange', label='Outer Boundary', bottom=df_clean['Inner Boundary (km)'])

plt.xticks(rotation=90)
plt.xlabel('Feature')
plt.ylabel('Distance from Saturn (km)')
plt.title('Feature Boundaries in Relation to Distance from Saturn, Excluding Phoebe Ring')
plt.legend()
plt.tight_layout()

# Show the plot
plt.show()
