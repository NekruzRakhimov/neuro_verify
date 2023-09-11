import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/process_photo', methods=['POST'])
def process_photo():
    file = request.files['photo']
    result = process_image(file)
    response = {'result': result}
    return jsonify(response)


@app.route('/', methods=['GET'])
def ping():
    response = {'result': 'server is up and running'}
    return jsonify(response)


def process_image(file):
    return True


if __name__ == '__main__':
    # Получение адреса и порта из переменных окружения
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))

    # Запуск сервера Flask
    app.run(host='0.0.0.0', port=port)
