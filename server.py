from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Licenszkulcsok listája lejárati dátummal
licenses = {
    "XYZ789": "2023-01-01",  # Ez már lejárt
    "1198kji@gmir": "2050-10-20"
}

@app.route("/api/license/<key>")
def validate_license(key):
    expiry = licenses.get(key)
    if expiry:
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d")
        if expiry_date < datetime.now():
            return jsonify({"valid": False, "reason": "expired"})
        else:
            return jsonify({"valid": True})
    else:
        return jsonify({"valid": False, "reason": "invalid"})

if __name__ == "__main__":
    app.run(host="0.0.0.0")
