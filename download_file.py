import requests
from pathlib import Path


def downloads_file(url, folder, file_name, **kwargs):
    """Скачивание и сохранение файла"""
    response = requests.get(url, params=kwargs)
    response.raise_for_status()
    with open(f'{Path(folder).joinpath(file_name)}', 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    downloads_file()
