FROM python:3.7-alpine

COPY bots/config.py /bots/
COPY bots/bot.py /bots/
COPY bots/credentials.py /bots/
copy bots/imageSearch.py /bots/
COPY requirements.txt /tmp
COPY image-name.txt /
COPY image/moon.jpg /image/
COPY image/sunrise.jpg /image/
RUN pip3 install -r /tmp/requirements.txt

CMD ["python3", "bots/bot.py"]
