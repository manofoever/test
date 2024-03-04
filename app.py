from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ask_me', methods = ['POST'])
def get_json_data():
    data = {"message" : "Hello, what do you want?"}
    return jsonify(data)

@app.route('/ask_me_anything')
def get_data():
    data = {"message" : "Hello, what do you want?"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
