import mlib
import logging
from flask import Flask, request, jsonify
from flask.logging import create_logger

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route("/")
def home():
    html = f"<h3>Predict the height from weight of MLB players</h3>"
    return html.format(format)


@app.route("/predict", methods=["POST"])
def predict():
    json_payload = request.json
    LOG.info(f"JSON payload: {json_payload}")
    prediction = mlib.predict(json_payload["Weight"])
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
