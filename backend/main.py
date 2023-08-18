from flask import Flask, jsonify
from flask_cors import CORS
# TODO venv ficar dentro do backend

app = Flask(__name__)
CORS(app)  # Isso habilitará o CORS para todas as rotas


@app.route("/api/data")
def get_data():
    data = {"message": "Hello from Flask!"}
    return jsonify(data)


@app.route("/api/test")
def test():
    data = {"message": "Test endpoint working!"}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
