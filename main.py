from flask import Flask, request, jsonify, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 API تعمل بنجاح! استخدم /generate_qr لإنشاء QR."

@app.route('/generate_qr', methods=['GET'])
def generate_qr():
    data = request.args.get('data')
    color = request.args.get('color', 'black')  # اللون الافتراضي أسود
    size = int(request.args.get('size', 300))   # الحجم الافتراضي 300x300
    
    if not data:
        return jsonify({"error": "يرجى إدخال البيانات عبر ?data=yourtext"}), 400

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color="white")
    
    # حفظ الصورة في الذاكرة وإرسالها كملف
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
