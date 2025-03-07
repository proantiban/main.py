from flask import Flask, request, jsonify
import aiohttp
import asyncio

app = Flask(__name__)

API_URL = "https://ff-community-api.vercel.app/ff.Info"

async def send_single_visitor(uid):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{API_URL}?uid={uid}") as response:
                return response.status == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

async def send_visitors(uid, num_visitors=100):
    success_count = 0
    for _ in range(num_visitors):
        success = await send_single_visitor(uid)
        if success:
            success_count += 1
        await asyncio.sleep(0.1)  # انتظار 100 مللي ثانية بين كل طلب لتجنب الضغط على السيرفر
    return success_count

@app.route('/')
def home():
    return "🚀 API يعمل بنجاح!"

@app.route('/send_visitors', methods=['GET'])
async def api_send_visitors():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"error": "يرجى إدخال UID"}), 400

    success_count = await send_visitors(uid)
    return jsonify({"uid": uid, "total_requested": 100, "successful_visits": success_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
