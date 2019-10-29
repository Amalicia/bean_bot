from config import create_api
from imageSearch import get_image
from datetime import date
import tweepy
import schedule
import time
import logging
import random
import os

month_dict = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}

logger = logging.getLogger()


def update_status(api, image, message):
    api.update_with_media(image, message)
    logger.info("Tweet sent")
    # os.remove(image)
    logger.info("Image deleted")


def format_weather_string():
    today = date.today()
    return "Weather for {} {} {}: Sunny with a hint of beans".format(today.day, month_dict[today.month], today.year)


def format_morning_string():
    today = date.today()
    return "Good Morning! ({} {} {})".format(today.day, month_dict[today.month], today.year)


def format_night_string():
    today = date.today()
    return "Good Night! ({} {} {})".format(today.day, month_dict[today.month], today.year)


def get_image_name():
    file = open("image-name.txt", "r")
    contents = file.read()
    file.close()
    return contents


def main():
    api = create_api()
    schedule.every().day.at("07:00").do(update_status, api, "./image/sunrise.jpg", format_morning_string())
    schedule.every().day.at("12:30").do(get_image, "baked beans")
    schedule.every().day.at("13:00").do(update_status, api, get_image_name(), format_weather_string())
    schedule.every().day.at("22:00").do(update_status, api, "./image/moon.jpg", format_night_string())
    while True:
        schedule.run_pending()
        time.sleep(random.randint(600, 1800))


if __name__ == "__main__":
    main()
