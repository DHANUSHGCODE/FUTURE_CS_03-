from flask import Flask, request, render_template
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

app = Flask(__name__)
KEY = get_random_bytes(16)

@app.route('/')
def home():
    return render_template('upload.html')

def encrypt(data):
    cipher = AES.new(KEY, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce + ciphertext

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    encrypted = encrypt(file.read())
    with open("encrypted_files/" + file.filename, "wb") as f:
        f.write(encrypted)
    return "File uploaded and encrypted"

if __name__ == '__main__':
    app.run(debug=True)
