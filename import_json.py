import json

filename = input("Enter JSON file name: ")

try:
    with open(filename, "r") as file:
        data = json.load(file)

    print("\nJSON Data")
    print("----------")

    for key, value in data.items():
        print(f"{key} : {value}")

except FileNotFoundError:
    print("File not found!")

except json.JSONDecodeError:
    print("Invalid JSON file!")