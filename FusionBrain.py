import json
import time

import requests
import base64

class FusionBrainAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_pipeline(self):
        response = requests.get(self.URL + 'key/api/v1/pipelines', headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, pipeline_id, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": "{prompt}"
            }
        }

        data = {
            'pipeline_id': (None, pipeline_id),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/pipeline/run', headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/pipeline/status/' + request_id, headers=self.AUTH_HEADERS)
            data = response.json()
            if data['status'] == 'DONE':
                return data['result']['files']

            attempts -= 1
            time.sleep(delay)


if __name__ == '__main__':
    api = FusionBrainAPI('https://api-key.fusionbrain.ai/', '33CB1D0903AF9D5768BBECE0728B4B35', '94B842228D5E888E2407186CA29F0F93')
    pipeline_id = api.get_pipeline()
    uuid = api.generate("Sun in sky", pipeline_id)
    files = api.check_generation(uuid)
    print(files)
    # Здесь image_base64 - это строка с данными изображения в формате base64

    image_base64 = files[0]  # Вставьте вашу строку base64 сюда

    # Декодируем строку base64 в бинарные данные

    image_data = base64.b64decode(image_base64)

    # Открываем файл для записи бинарных данных изображения

    with open("image.jpg", "wb") as file:

        file.write(image_data)

#Не забудьте указать именно ваш YOUR_KEY и YOUR_SECRET.