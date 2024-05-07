FROM python
WORKDIR /UNO_GAME
COPY . /UNO_GAME
CMD ["python3", "main.py"]