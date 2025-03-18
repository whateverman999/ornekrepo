## Hatalı Erişim Kontrolü Örnek 1

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_page():
    return 'Hoşgeldiniz.'

@app.route('/user/<int:id>')
def profile(id):
    # Erişim kontrolü problem örneği
    return '{0} nolu id degerine sahip user'.format(id)
```
