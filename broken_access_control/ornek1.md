## Hatalı Erişim Kontrolü Örnek 1

- Missing authentication
- Kimlik doğrulama uygulanmalıydı

```python
from flask import Flask

app = Flask(__name__)

@app.route('/settings/<int:user_id>')
def profile(user_id):
    # Erişim kontrolü problem örneği
    return '{0} nolu id degerine sahip kullanici ayar sayfasi'.format(user_id)
```
