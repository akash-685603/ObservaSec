from flask import Flask, jsonify
import logging, os, time
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# log to file
LOG_DIR = "/var/log/observasec"
os.makedirs(LOG_DIR, exist_ok=True)
file_handler = RotatingFileHandler(f"{LOG_DIR}/app.log", maxBytes=10*1024*1024, backupCount=3)
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
file_handler.setLevel(logging.INFO)

# also log to stdout (picked by K8s + Filebeat)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
stream_handler.setLevel(logging.INFO)

app.logger.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.addHandler(stream_handler)

@app.route("/")
def home():
    app.logger.info("hit /")
    return jsonify(project="ObservaSec", msg="Hello from ObservaSec", ts=time.time())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
