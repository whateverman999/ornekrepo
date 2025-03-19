from flask import Flask
import jwt

@app.route("/deneme")
def deneme():

encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])

## Hatalı Erişim Kontrol Örnek 5

- TASLAK: JWT Örneği Buraya Gelecek