from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    return render_template('data_analyzer.html')

@app.route('/store', methods=['POST'])
def store():
    global stored_url
    data = request.get_json()
    URL = data.get('value')
    print(URL)
    stored_url = URL
    result = subprocess.run(['python3', 'scrappy/table_spider.py', URL], capture_output=True, text=True)
    
    image1_path= "graph_1.png"
    image2_path= "graph_2.png"
    image3_path= "graph_3.png"
    
    return jsonify(image_path=image1_path)

@app.route('/get_url')
def get_url():
    return jsonify(url=stored_url)

if __name__ == '__main__':
    app.run(debug=True)

