from flask import Flask, request, jsonify

app = Flask(__name__)

# قائمة الانتظار (Queue)
queue = []

@app.route('/')
def home():
    return "🚀 Queue API يعمل بنجاح!"

# إضافة شخص إلى قائمة الانتظار
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "يرجى إرسال الاسم بصيغة JSON"}), 400

    user_id = len(queue) + 1
    queue.append({"id": user_id, "name": data["name"]})

    return jsonify({"message": "تمت الإضافة بنجاح", "queue_position": user_id})

# عرض قائمة الانتظار
@app.route('/queue', methods=['GET'])
def get_queue():
    return jsonify(queue)

# حذف أول شخص في قائمة الانتظار
@app.route('/complete_user', methods=['POST'])
def complete_user():
    if queue:
        completed_user = queue.pop(0)
        return jsonify({"message": "تم إكمال الدور", "completed_user": completed_user})
    return jsonify({"error": "القائمة فارغة"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
