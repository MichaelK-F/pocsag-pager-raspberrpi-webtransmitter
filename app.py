from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    command = request.form['command']
    result = subprocess.getoutput(command)
    return jsonify({'output': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
