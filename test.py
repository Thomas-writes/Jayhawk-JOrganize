from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('data_analyzer.html')

def get_info():
    data = request.get_json()
    URL = data.get('value')
    print(f"{URL}")

if __name__ == '__main__':
    app.run()