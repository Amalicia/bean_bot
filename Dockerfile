FROM python:3.7-alpine

COPY bots/config.py /bots/
COPY bots/bot.py /bots/
COPY bots/credentials.py /bots/
copy bots/imageSearch.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "bot.py"]
