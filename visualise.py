import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the JSON data (make sure the file is available in the same directory or provide correct path)
with open('AGRI.json', 'r') as file:
    data = [json.loads(line) for line in file]

# Convert JSON data to a Pandas DataFrame
df = pd.json_normalize(data)

# Limit data to a smaller subset for testing purposes (adjust sample size)
df = df.head(100)  # Adjust the number of rows as needed

# Display the first few rows to understand the structure
print(df.head())

# Ensure the date column is in datetime format (if needed)
df['date'] = pd.to_datetime(df['date'])

# Visualization 1: Scatter plot for soil pH level vs. crop yield estimate
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='soil.ph_level', y='crop.yield_estimate', hue='crop.disease_outbreak', palette='coolwarm')
plt.title('Soil pH Level vs Crop Yield Estimate')
plt.xlabel('Soil pH Level')
plt.ylabel('Yield Estimate')
plt.legend(title='Disease Outbreak')
plt.show()

# Visualization 2: Line plot for temperature trends (soil vs weather) over time
df = df.sort_values('date')  # Sort by date

plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['soil.temperature'], label='Soil Temperature (°C)', marker='o')
plt.plot(df['date'], df['weather.temperature'], label='Weather Temperature (°C)', marker='x')
plt.title('Temperature Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.show()

# Visualization 3: Bar plot for yield estimates by region
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='location.region', y='crop.yield_estimate', hue='crop.type', palette='viridis')
plt.title('Yield Estimate by Region')
plt.xlabel('Region')
plt.ylabel('Yield Estimate')
plt.xticks(rotation=45)
plt.legend(title='Crop Type')
plt.show()

# Visualization 4: Soil pH Level vs Yield Estimate with Soil Moisture as Hue
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='soil.ph_level', y='crop.yield_estimate', hue='soil.moisture', palette='coolwarm')
plt.title('Soil pH Level vs Crop Yield Estimate with Soil Moisture as Hue')
plt.xlabel('Soil pH Level')
plt.ylabel('Yield Estimate')
plt.legend(title='Soil Moisture')
plt.show()

# Visualization 5: Temperature vs Yield Estimate by Growth Stage (Line Plot)
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='date', y='soil.temperature', hue='crop.growth_stage', marker='o', label='Soil Temperature (°C)')
sns.lineplot(data=df, x='date', y='weather.temperature', hue='crop.growth_stage', marker='x', label='Weather Temperature (°C)')
plt.title('Temperature vs Yield Estimate by Growth Stage')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend(title='Growth Stage')
plt.show()

# Visualization 6: Rainfall vs Yield Estimate (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='weather.rainfall', y='crop.yield_estimate', hue='crop.disease_outbreak', palette='coolwarm')
plt.title('Rainfall vs Crop Yield Estimate')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Yield Estimate')
plt.legend(title='Disease Outbreak')
plt.show()

# Visualization 7: Humidity vs Disease Outbreak (Bar Plot)
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='weather.humidity', y='crop.disease_outbreak', hue='crop.type', palette='viridis')
plt.title('Humidity vs Disease Outbreak by Crop Type')
plt.xlabel('Humidity (%)')
plt.ylabel('Disease Outbreak Frequency')
plt.legend(title='Crop Type')
plt.show()

# Visualization 8: Correlation Heatmap
correlation_data = df[['soil.ph_level', 'soil.moisture', 'soil.temperature', 'weather.temperature',
                       'weather.humidity', 'weather.rainfall', 'weather.wind_speed', 'crop.yield_estimate']]

correlation_matrix = correlation_data.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of Environmental and Crop Factors')
plt.show()
