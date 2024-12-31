from flask import Flask, jsonify, request
import csv

app = Flask(__name__)


# Function to read CSV data
def read_csv():
    data = []
    with open('crime.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


# Function to write data to CSV file
def write_to_csv(new_crime):
    fieldnames = ['State', 'Years', 'Homicides', 'Rape', 'Robbery']  # Adjust fieldnames as per your CSV structure
    with open('crime.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(new_crime)


@app.route('/', methods=['GET'])
def get_crimes():
    data = read_csv()
    return jsonify(data)


@app.route('/', methods=['POST'])
def add_crime():
    new_crime = request.get_json()  # Get JSON data from POST request body
    write_to_csv(new_crime)  # Add new data to CSV file
    return jsonify({"message": "Crime added successfully"}), 201


if __name__ == '__main__':
    app.run(debug=True)
