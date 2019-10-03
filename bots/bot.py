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


def update_status(api, image):
    today = date.today()
    # api.update_with_media(image, "Weather for {} {} {}: Sunny with a hint of beans"
    #                       .format(today.day, month_dict[today.month], today.year))
    api.update_with_media(image, "This is a test")

    logger.info("Tweet sent")
    os.remove(image)
    logger.info("Image deleted")


def get_image_name():
    file = open("image-name.txt", "r")
    return file.read()


def main():
    api = create_api()
    get_image("baked beans")
    update_status(api, get_image_name())
    # schedule.every().day.at("13:00").do(update_status, api)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(random.randint(600, 1800))


if __name__ == "__main__":
    main()
