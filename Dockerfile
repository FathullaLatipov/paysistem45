# Какой язык программирования
FROM python:latest
# Копируем всеъ файлов
COPY ./project
# Назначить основную нашу папку для Docker
WORKDIR /project

# Установка наших библиотек
RUN pip install -r requirements.txt

# Запуск проекта
CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0", "--port=2323"]