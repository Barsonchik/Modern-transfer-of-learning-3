import requests

# URL файла
url = "https://gbcdn.mrgcdn.ru/uploads/asset/5963559/attachment/74518604a7920dfa8e79c9d67da99185.ipynb"

# Скачивание файла
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Сохранение файла
    with open("downloaded_file3.ipynb", "wb") as file:
        file.write(response.content)
    print("Файл успешно скачан и сохранен как 'downloaded_file.ipynb'.")
else:
    print("Ошибка при скачивании файла:", response.status_code)