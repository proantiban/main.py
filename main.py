from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# API Endpoint
API_URL = "https://ff-community-api.vercel.app/ff.Info"

@app.route('/')
def home():
    return "🚀 API يعمل بنجاح!"

@app.route('/send_visitors', methods=['GET'])
def send_visitors():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"error": "يرجى إدخال UID"}), 400

    num_visitors = 100  # عدد الزوار ثابت
    success_count = 0

    for _ in range(num_visitors):
        response = requests.get(f"{API_URL}?uid={uid}")
        if response.status_code == 200:
            success_count += 1

    return jsonify({"uid": uid, "total_requested": num_visitors, "successful_visits": success_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
