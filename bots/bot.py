import tweepy
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


def main():
    api = create_api()
    today = date.today()
    api.update_status("Weather for {} {} {}: Sunny with a hint of beans"
                      .format(today.day, month_dict[today.month], today.year))


if __name__ == "__main__":
    main()
