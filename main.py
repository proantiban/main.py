from flask import Flask, request, jsonify

app = Flask(__name__)

# قائمة الانتظار
queue = []

@app.route('/')
def home():
    return "🚀 Queue API يعمل بنجاح!"

# إضافة شخص إلى قائمة الانتظار
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    if not data or "name" not in data:
        return jsonify({"error": "يرجى إدخال اسم المستخدم"}), 400
    
    user = {"id": len(queue) + 1, "name": data["name"]}
    queue.append(user)
    
    return jsonify({"message": "تمت إضافة المستخدم بنجاح!", "user": user})

# جلب قائمة الانتظار
@app.route('/get_queue', methods=['GET'])
def get_queue():
    return jsonify({"queue": queue})

# إزالة أول شخص من قائمة الانتظار
@app.route('/remove_user', methods=['POST'])
def remove_user():
    if not queue:
        return jsonify({"error": "لا يوجد أشخاص في قائمة الانتظار"}), 400
    
    removed_user = queue.pop(0)
    return jsonify({"message": "تمت إزالة المستخدم", "user": removed_user})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
