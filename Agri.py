import random
import json
from faker import Faker

# Create an instance of the Faker class
fake = Faker()

# Number of records to generate
num_records = 100000

# Function to generate random geographical location data
def generate_location():
    return {
        "region": fake.city(),
        "latitude": round(random.uniform(30.0, 40.0), 2),
        "longitude": round(random.uniform(-120.0, -110.0), 2)
    }

# Function to generate soil data
def generate_soil():
    return {
        "ph_level": round(random.uniform(5.5, 7.5), 2),
        "moisture": round(random.uniform(20.0, 30.0), 2),
        "temperature": round(random.uniform(15.0, 25.0), 1),
        "organic_matter": round(random.uniform(2.0, 5.0), 1),
        "nutrients": {
            "nitrogen": round(random.uniform(10.0, 15.0), 1),
            "phosphorus": round(random.uniform(8.0, 12.0), 1),
            "potassium": round(random.uniform(12.0, 18.0), 1)
        }
    }

# Function to generate weather data
def generate_weather():
    return {
        "temperature": round(random.uniform(10.0, 20.0), 1),
        "humidity": random.randint(60, 80),
        "rainfall": round(random.uniform(0.0, 10.0), 1),
        "wind_speed": round(random.uniform(5.0, 15.0), 1)
    }

# Function to generate crop data
def generate_crop():
    crops = ["Wheat", "Corn", "Rice", "Soybean", "Barley"]
    growth_stages = ["Germination", "Vegetative", "Flowering", "Maturation"]

    return {
        "type": random.choice(crops),
        "growth_stage": random.choice(growth_stages),
        "yield_estimate": random.randint(1000, 5000),
        "disease_outbreak": random.choice([True, False])
    }

# Generate all records
agriculture_data = []
for record_id in range(1, num_records + 1):
    record = {
        "record_id": record_id,
        "location": generate_location(),
        "date": "" + fake.date(),
        "soil": generate_soil(),
        "weather": generate_weather(),
        "crop": generate_crop()
    }
    agriculture_data.append(record)

# Function to save the generated data to a JSON lines file
def save_to_json_lines(filename, data):
    with open(filename, "w") as f:
        for record in data:
            f.write(json.dumps(record) + "\n")

# Save the generated data to a JSON lines file
save_to_json_lines("agriculture_data2.jsonl", agriculture_data)

print("Data saved as JSON lines file in the current directory.")