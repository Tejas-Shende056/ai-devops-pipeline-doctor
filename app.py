from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "healthy", "message": "DevOps Pipeline Doctor App Running"})

@app.route("/calculate/<int:a>/<int:b>")
def calculate(a, b):
    # Intentional division bug for testing later if needed
    result = a / b
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)