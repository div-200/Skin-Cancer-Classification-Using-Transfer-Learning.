
from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return jsonify({
            "message": "Please upload an image."
        }), 400

    file = request.files["file"]

    if not file.filename:
        return jsonify({
            "message": "No image selected."
        }), 400

    if not file.mimetype.startswith("image/"):
        return jsonify({
            "message": "Please upload an image."
        }), 400

    return jsonify({
        "message": "Image uploaded successfully! Connect the trained MobileNetV2 model for actual skin lesion classification. Please consult a dermatologist for diagnosis."
    })

if __name__ == "__main__":
    app.run(debug=False)
  
