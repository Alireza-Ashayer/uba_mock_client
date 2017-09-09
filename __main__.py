import sys
import os
from random import randint
import time
from optparse import OptionParser
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from threading import Thread


def send_request(url):

    gender_rand = randint(0, 1)
    gender = "male"
    if gender_rand == 0:
        gender = "female"
    else:
        gender = "male"

    post_fields = {"Category": "swipe", "Gender" : gender}

    request = Request(url, urlencode(post_fields).encode())
    return urlopen(request)


def send_requests(url, rate):
    for i in range(0, int(rate)):
        Thread(target=send_request, args=[url]).start()

    print("%s requests sent" % rate)


def main():

    # parse parameters
    parser = OptionParser()
    parser.add_option("-r", "--rate", action="store", dest="rate")
    parser.add_option("-u", "--url", action="store", dest="url")
    (options, args) = parser.parse_args()
    rate = options.rate
    url = options.url

    # check parameters validity
    if rate is None:
        raise ValueError("Please specify request rate per second using -r or --rate")

    try:
        int(rate)
    except ValueError:
        raise ValueError("rate is not of integer type")

    if url is None:
        raise ValueError("Please specify a url using -u or --url")

    # start a timer to send requests
    while True:
        Thread(target=send_requests, args=[url, rate]).start()
        time.sleep(1)


if __name__ == "__main__":
    main()





