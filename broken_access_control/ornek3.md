## Hatalı Erişim Kontrolü Örnek 4

- CWE-598: Use of GET Request Method With Sensitive Query Strings

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/user_login/')
def user_info():
    # Erişim kontrolü problem örneği 3
    username = request.args.get('username')
    password = request.args.get('password')
    # Giriş işlemleri operasyonu  
    return 'Logged in as {0}'.format(username)
```