import os
from flask import Flask, request, jsonify
import random
from PIL import Image
from deepface import DeepFace

app = Flask(__name__)


@app.route('/process_photo', methods=['POST'])
def process_photo():
    file = request.files['selfie']
    result = process_image(file)
    response = {'result': result}
    return jsonify(response)


@app.route('/', methods=['GET'])
def ping():
    response = {'result': 'server is up and running'}
    return jsonify(response)


def process_image(file):
    return random.choice([True, False])


def compare_passport_and_person(image_path):
    # Загрузка изображения
    image = Image.open(image_path)

    # Разделение изображения на две части
    width, height = image.size
    half_width = width // 2

    person_image = image.crop((0, 0, int(width * 0.7), height))
    passport_image = image.crop(0, (int(width * 0.3), width, height))

    # Преобразование изображений в формат, подходящий для Deepface
    person_image_path = "person_temp.jpg"
    passport_image_path = "passport_temp.jpg"

    person_image.save(person_image_path)
    passport_image.save(passport_image_path)

    # Сравнение лиц
    result = compare_faces(person_image_path, passport_image_path)

    # Удаление временных файлов
    os.remove(person_image_path)
    os.remove(passport_image_path)

    return result


def compare_faces(image1_path, image2_path):
    # Загрузка изображений
    image1 = DeepFace.detectFace(img_path=image1_path, enforce_detection=False)
    image2 = DeepFace.detectFace(img_path=image2_path, enforce_detection=False)

    # Rfhfvekmner!979
    # Проверка наличия лица на изображениях
    if image1 is None or image2 is None:
        return False

    # Сравнение лиц
    result = DeepFace.verify(image1, image2)

    # Проверка результата
    if result["verified"]:
        return True
    else:
        return False


if __name__ == '__main__':
    # Получение адреса и порта из переменных окружения
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))

    # Запуск сервера Flask
    app.run(host='0.0.0.0', port=port)
