from flask import Flask, request, jsonify, send_file
from flask_cors import CORS  # Mengimpor CORS

app = Flask(__name__)
CORS(app)  # Mengaktifkan CORS untuk seluruh aplikasi

# Daftar key yang valid
VALID_KEYS = ["Ghv218yhawFFG", "7NDH9a0g9Bs"]

@app.route('/validate-key', methods=['POST'])
def validate_key():
    try:
        # Menerima key dari frontend
        data = request.json
        key = data.get('key')

        # Validasi key
        if key in VALID_KEYS:
            return jsonify({"valid": True})
        else:
            return jsonify({"valid": False}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download', methods=['GET'])
def download_file():
    try:
        # Mengirimkan file extension.zip jika validasi sukses
        return send_file("extension.zip", as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
