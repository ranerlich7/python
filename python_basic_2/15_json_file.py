import json
data = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "San Francisco"}
]
# Specify the path to your JSON file
file_path = 'data.json'

# Open the file in write mode
with open(file_path, 'w') as f:   # f=open()
    json.dump(data, f)

#########################################
# Read data from the JSON file
with open(file_path, 'r') as f:
    loaded_data = json.load(f)

print(f"Data loaded from {file_path}: {loaded_data[0]["name"]}")


