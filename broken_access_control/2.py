from flask import Flask, request

app = Flask(__name__)

@app.route('/administration')
def administration():
    # Erişim kontrolü problem örneği 2
    username = request.cookies.get('username')
    return 'Yönetim Sayfası'