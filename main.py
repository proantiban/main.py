from flask import Flask, request, jsonify
import aiohttp
import asyncio

app = Flask(__name__)

API_URL = "https://ff-community-api.vercel.app/ff.Info"

async def send_visitors(uid, num_visitors=25):
    async with aiohttp.ClientSession() as session:
        tasks = [session.get(f"{API_URL}?uid={uid}") for _ in range(num_visitors)]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        success_count = sum(1 for res in responses if isinstance(res, aiohttp.ClientResponse) and res.status == 200)
        return success_count

@app.route('/')
def home():
    return "🚀 API يعمل بنجاح!"

@app.route('/send_visitors', methods=['GET'])
async def api_send_visitors():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"error": "يرجى إدخال UID"}), 400

    success_count = await send_visitors(uid, 25)  # إرسال 25 طلب دفعة واحدة
    return jsonify({"uid": uid, "total_requested": 25, "successful_visits": success_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
