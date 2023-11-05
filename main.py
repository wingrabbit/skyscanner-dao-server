from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/status")
def home():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True)