import requests
import uuid
from config.settings import BASE_DIR
from celery import shared_task

CAT_URL = 'https://cataas.com/cat'

@shared_task
def download():
    response = requests.get(CAT_URL)
    file_extinsoin = response.headers.get("Content-Type").split('/')[1]
    file_name = BASE_DIR / 'cats' / (f'{str(uuid.uuid4())}.{file_extinsoin}')
    with open(file_name, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)
    return