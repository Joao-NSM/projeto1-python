from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def teste1():
    return jsonify({'message' : 'Hello Calculador'})


if __name__ == "__main__" : 
    app.run(host='0.0.0.0', port=5000) 

