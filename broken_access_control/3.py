from flask import Flask, request

app = Flask(__name__)

@app.route('/user_login/')
def user_info():
    # Erişim kontrolü problem örneği 3
    username = request.args.get('username')
    password = request.args.get('password')
    # Giriş işlemleri operasyonu  
    return 'Logged in as {0}'.format(username)