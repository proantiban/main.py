from flask import Flask, request, jsonify

app = Flask(__name__)

# قائمة الانتظار
queue = []
counter = 1  # الرقم التسلسلي

@app.route("/")
def home():
    return "🚀 Queue API يعمل بنجاح!"

# إضافة شخص إلى قائمة الانتظار
@app.route("/add", methods=["POST"])
def add_to_queue():
    global counter
    name = request.json.get("name")
    if not name:
        return jsonify({"error": "يرجى إدخال الاسم"}), 400
    
    queue.append({"id": counter, "name": name})
    counter += 1
    return jsonify({"message": f"{name} تم إضافته إلى قائمة الانتظار", "position": len(queue)})

# الحصول على قائمة الانتظار
@app.route("/queue", methods=["GET"])
def get_queue():
    return jsonify({"queue": queue})

# حذف شخص من قائمة الانتظار بعد انتهاء دوره
@app.route("/remove", methods=["POST"])
def remove_from_queue():
    if not queue:
        return jsonify({"error": "قائمة الانتظار فارغة"}), 400
    
    removed = queue.pop(0)
    return jsonify({"message": f"تم إزالة {removed['name']} من قائمة الانتظار", "remaining_queue": queue})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
