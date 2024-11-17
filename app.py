from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
import subprocess
import os
from graph_maker import create_graphs
import matplotlib
matplotlib.use('Agg')

app = Flask(__name__)
app.secret_key = 'key'
CORS(app)

@app.route("/")
def main():
    return render_template('data_analyzer.html')

@app.route('/store', methods=['POST'])
def store():
    data = request.get_json()
    URL = data.get('value')
    print(URL)
    session['stored_url'] = URL
    subprocess.run(['python3', 'scrappy/table_spider.py', URL], capture_output=True, text=True)
    
    graph_output_files = create_graphs()
    
    return jsonify({
            "graph_1": graph_output_files[0],
            "graph_2": graph_output_files[1],
            "graph_3": graph_output_files[2]
        })

@app.route('/get_url')
def get_url():
    url = session.get('stored_url', None)
    return jsonify(url=url)

if __name__ == '__main__':
    app.run(debug=True)

