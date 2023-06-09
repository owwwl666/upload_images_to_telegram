def reads_file(path):
    """Открытие и чтение файла"""
    with open(path, 'rb') as file:
        reading = file.read()
    return reading


if __name__ == '__main__':
    reads_file()
