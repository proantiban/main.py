from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def send_visitors(uid, num_visitors=100):
    url = f"https://ff-community-api.vercel.app/ff.Info?uid={uid}"
    success_count = 0
    for _ in range(num_visitors):
        response = requests.get(url)
        if response.status_code == 200:
            success_count += 1
    return success_count

@app.route('/send_visitors', methods=['GET'])
def api_send_visitors():
    uid = request.args.get('uid')
    num_visitors = int(request.args.get('num_visitors', 100))  
    if not uid:
        return jsonify({"error": "يجب إدخال UID"}), 400

    success_count = send_visitors(uid, num_visitors)
    return jsonify({"uid": uid, "requested": num_visitors, "successful_visits": success_count})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
