from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Привет, это локальный сервер на Flask!"

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)