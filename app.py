from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fila')
def fila():
    return render_template('fila.html')

@app.route('/fila-circular')
def fila_circular():
    return render_template('fila_circular.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)