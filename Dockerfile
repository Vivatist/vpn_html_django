# Создать образ на основе базового слоя,
# который содержит файлы ОС и интерпретатор Python 3.9.
FROM python:3.11
# Перейти в образе в директорию /app: в ней будет храниться код проекта.
# Если директории с таким именем нет, она будет создана.
# Название директории может быть любым.
WORKDIR /app

RUN pip install gunicorn==20.1.0 
# Дальнейшие инструкции будут выполняться в директории /app
# Скопировать с локального компьютера файл зависимостей
# в текущую директорию образа (текущая директория — это /app).
COPY requirements.txt .
# Выполнить в текущей директории образа команду терминала
# для установки зависимостей.
RUN pip install -r requirements.txt --no-cache-dir
# Скопировать всё необходимое содержимое
# той директории локального компьютера, где сохранён Dockerfile,
# в текущую рабочую директорию образа — /app.
COPY . .
# При старте контейнера запустить сервер разработки.
#CMD ["python", "manage.py", "runserver", "0:8000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "sssvpn.wsgi"] 