FROM python:3.10.12-slim
ENV TOKEN='6321515099:AAFh0-u1zNRgRBlizey0oDfzSUU3mG60NwI'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py"]