FROM python:3.10.12-slim
ENV TOKEN='You token'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py"]
