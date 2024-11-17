from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import subprocess


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
    URL = '"' +  URL + '"'
    print(URL)
    stored_url = URL
    result = subprocess.run(['python3', 'test2.py', URL], capture_output=True, text=True)
    print(result.stdout.strip('\n'))
    return jsonify(message=stored_url)

@app.route('/get_url')
def get_url():
    return jsonify(url=stored_url)

if __name__ == '__main__':
    app.run(debug=True)

