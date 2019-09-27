import tweepy
import schedule
import time
import logging
import random
from config import create_api
from datetime import date

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


def update_status(api):
    today = date.today()
    api.update_status("Weather for {} {} {}: Sunny with a hint of beans"
                      .format(today.day, month_dict[today.month], today.year))
    logger.info("Tweet sent")


def main():
    api = create_api()
    schedule.every().day.at("13:00").do(update_status, api)
    while True:
        schedule.run_pending()
        time.sleep(random.randint(600, 1800))


if __name__ == "__main__":
    main()
