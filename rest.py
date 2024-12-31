# import pandas as pd
# from flask import Flask, render_template, request, redirect, url_for , jsonify
#
#
# app = Flask(__name__)
#
# crime_data = pd.read_csv('crime.csv')
#
# @app.route('/get_form', methods=['GET'])
# def get_crime_data():
#     year = request.args.get('year')
#     state = request.args.get('state')
#     crime_type = request.args.get('crime_type')
#
#     return render_template('get_form.html')
#
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
# if __name__ == '__main__':
#     app.run(debug=True)



import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load your crime data CSV file
crime_data = pd.read_csv('crime.csv')

@app.route('/get_form', methods=['GET'])
def get_crime_data():
    year = request.args.get('year')
    state = request.args.get('state')
    crime_type = request.args.get('crime_type')

    filtered_data = crime_data  # Initialize with the original DataFrame

    # if year:
    #     filtered_data = filtered_data[filtered_data['Year'] == int(year)]
    # if state:
    #     filtered_data = filtered_data[filtered_data['State'] == state]
    # if crime_type:
    #     filtered_data = filtered_data[filtered_data['Crime Type'] == crime_type]

    # Convert the filtered data to JSON and return it
    return jsonify(filtered_data.to_dict(orient='records'))

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
