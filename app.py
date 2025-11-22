import json

with open("data.json", "r") as f:
    data = json.load(f)

print("Name: ", data['name'])
print("Age: ", data["age"])