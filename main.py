from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://ff-community-api.vercel.app/ff.Info"

def send_visitors(uid, num_visitors=25):
    success_count = 0
    for _ in range(num_visitors):
        try:
            response = requests.get(f"{API_URL}?uid={uid}")
            if response.status_code == 200:
                success_count += 1
        except Exception as e:
            print(f"Error: {e}")
    return success_count

@app.route('/')
def home():
    return "🚀 API يعمل بنجاح!"

@app.route('/send_visitors', methods=['GET'])
def api_send_visitors():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"error": "يرجى إدخال UID"}), 400

    success_count = send_visitors(uid, 25)
    return jsonify({"uid": uid, "total_requested": 25, "successful_visits": success_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
