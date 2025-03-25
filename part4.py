from flask import Flask, request, jsonify
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to the Docker Data API!"

@app.route('/data', methods=['POST'])
def process_data():
    api_url = 'https://data.cityofnewyork.us/resource/qmcw-ur37.csv'
    
    try:
        response = requests.get(api_url, timeout=10)  # Set a timeout for reliability
        response.raise_for_status()
        
        # Read CSV content from API response
        df = pd.read_csv(pd.compat.StringIO(response.text))  # Convert text to readable CSV

        return jsonify({
            'message': 'Data processed successfully!',
        })

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
