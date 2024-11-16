from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    return render_template('data_analyzer.html')

@app.route('/store', methods=['POST'])
def store():
    data = request.get_json()
    URL = data.get('value')
    print(URL)
    return None


if __name__ == '__main__':
    app.run(debug=True)
