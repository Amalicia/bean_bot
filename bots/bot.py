import tweepy
from config import create_api
from datetime import date


def main():
    api = create_api()
    api.update_status("Weather for {}: Sunny with a hint of beans".format(date.today()))


if __name__ == "__main__":
    main()
