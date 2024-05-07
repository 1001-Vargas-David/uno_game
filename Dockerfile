FROM python:3.10

WORKDIR /uno_game

COPY . /uno_game

CMD ["python3", "main.py"]