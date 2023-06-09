import requests


def downloads_file(url, folder, file_name,**kwargs):
    """Скачивание и сохранение файла"""
    response = requests.get(url,params=kwargs)
    response.raise_for_status()
    with open(f'{folder}/{file_name}', 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    downloads_file()
