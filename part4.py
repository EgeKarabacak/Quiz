from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Sample CSV file for demonstration
data = [
    {"id": 1, "name": "Ege", "age": 29, "City": "Ottawa"},
    {"id": 2, "name": "Josh", "age": 30, "City": "Ottawa"},
    {"id": 3, "name": "Omar", "age": 35, "City": "Toronto"}
]
df = pd.DataFrame(data)

@app.route('/')
def hello():
    return "Welcome to the Data API!"

@app.route('/data', methods=['POST'])
def process_data():
    # In a real-world scenario, you would load a CSV file here
    # For simplicity, we're working with the preloaded `df` DataFrame
    # You can extend it to read from a CSV if needed
    
    # Example processing: calculate average age
    average_age = df['age'].mean()

    # Returning response
    return jsonify({
        'message': 'Data processed successfully!',
        'average_age': average_age
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)