## Hatalı Erişim Kontrolü Örnek 2

- Missing authorization
- Rol tabanlı erişim mekanizması uygulanmalıydı

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/administration')
def administration():
    # Erişim kontrolü problem örneği 2
    username = request.cookies.get('username')
    return 'Yönetim Sayfası'
```