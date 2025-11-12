from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message='Welcome to Edu-Vault!')

@app.route('/api')
def api():
    return jsonify(message='Welcome to Edu-Vault!')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
