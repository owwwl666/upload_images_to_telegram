# Космический телеграм

### Описание
Скачивание фото с запусков с SpaceX и снимков NASA планеты Земля и публикации их в собственный telegram канал

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

### Реализация скриптов для скачивания фото:
- Скачивание фотографий запуска со SpaceX реализовано в скрипте `fetch_spacex_images.py`.

  - Запуск скрипта с передачей id конкретного пуска:
  
    ```
    python fetch_spacex_images.py -id [IDENTIFIER]
    ```
  - Запуск скрипта и скачивание фото последнего пуска SpaceX (без передачи аргументов):
    
    ```
    python fetch_spacex_images.py
    ```

- Скачивание фотографий планеты Земля от сервиса NASA Epic реализовано в скрипте `fetch_nasa_epic_images.py`.
  
  - Запуск скрипта для скачивания фото по личному api_key (-key) и количеству фотографий для скачивания (-qp):
    
    ```
    python fetch_nasa_epic_images.py -key [API_KEY] -qp [QUANTITY_PHOTOS]
    ```
  - Запуск скрипта для скачивания фото по default (DEMO_KEY) api_key (без передачи аргументов):
    
    ```
    python fetch_nasa_epic_images.py
    ```
  
  ### Переменные окружения для публикации фото в Telegram канал
  
  - TELEGRAM_BOT_TOKEN=токен созданного чат-бота
  - TELEGRAM_CHAT_ID=ссылка на id канала (целое число)
  - PATH_TO_PHOTOS=путь до желаемого фото (НЕОБЯЗАТЕЛЬНОЕ ПОЛЕ)
  - PATH_TO_PHOTOS_DIRECTORY=путь до директории, где хранятся скачанные фото 
  
  ### Публикация фото в Telegram канал
  
  - Создаем чат-бота
  - Создаем телеграм канал и делаем бота администратором канала
  - Запускаем скрипт
   
    ```
    publication_one_photos.py
    ```
    
    для публикации в канал одно любое фото
    
  - Запускаем скрипт с необязательным аргументом -pause (целое число), в котором указываем в часах перерыв между публикациями фотографий в телеграм       канал 
  
    ```
    publication_all_photos.py -pause [PUBLICATION_PAUSE]
    ``` 
    
    для публикации в канал в рандомном порядке всех фото, находящихся в папке 'images' с интервалом времени, указанном в минутах.

  ### Результаты
  ![](https://github.com/owwwl666/upload_images_to_telegram/blob/main/directory.png)
  ![](https://github.com/owwwl666/upload_images_to_telegram/blob/main/telegram.png)
