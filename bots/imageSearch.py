from credentials import CUSTOM_SEARCH_API_KEY, FORMATTED_ENGINE_ID
import urllib.request
import urllib.error
import json
import random
import imghdr
import os
import logging

logger = logging.getLogger()


def create_request(search_term):
    page = random.randint(1, 10)
    formatted_search = search_term.replace(" ", "+")
    request = urllib.request.Request('https://www.googleapis.com/customsearch/v1?key=' + CUSTOM_SEARCH_API_KEY +
                                     '&cx=' + FORMATTED_ENGINE_ID + '&q=' + formatted_search + '&start=' + str(page) +
                                     '&searchType=image&rights=cc_publicdomain&imgSize=large&fileType=jpg&filter=1')
    logger.info("Url created: " + str(request))
    return request


def fetch_data(request):
    with urllib.request.urlopen(request) as result:
        data = result.read().decode('utf-8')
    return data


def get_random_image(data):
    json_data = json.loads(data)
    results = json_data['items']
    image_url = random.choice(results)['link']
    urllib.request.urlretrieve(image_url, "./image")
    image_type = imghdr.what("./image")
    if not type(image_type) is None:
        image_name = "./image." + image_type
        os.rename("./image", image_name)
    else:
        image_name = "./image"
    logger.info("Image saved as: " + image_name)
    return image_name


def print_to_file(image_name):
    file = open("image-name.txt", "w")
    file.write(image_name)
    file.close()
    logger.info("Output file written")


def get_image(search_term):
    error_occurred = True
    while error_occurred:
        error_occurred = False
        try:
            request = create_request(search_term)
            data = fetch_data(request)
            image = get_random_image(data)
            print_to_file(image)
        except urllib.error.HTTPError as e:
            logger.error("Whoops, got an error: " + str(e))
            error_occurred = True
        except TypeError as e:
            logger.error("Image returned was not valid, fetching another")
            error_occurred = True
