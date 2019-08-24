import random
import time
import logging
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import requests
from requests import ConnectionError


logging.basicConfig(filename="test.log",
                    filemode="w",
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%d-%M-%Y %H:%M:%S",
                    level=logging.DEBUG)


def print_task():
    count = 0
    while count > 100:
        logging.info('this is a print task')
        time.sleep(5)
        count += 1


def spider_task():
    url = 'https://www.baidu.com'
    for _ in range(10):
        try:
            response = requests.get(url)
            headers = response.headers
            logging.info(headers)
        except ConnectionError:
            logging.error('ConnectionError')
        time.sleep(20)


def process_task():
    with ProcessPoolExecutor() as executor:
        executor.map(random_calculation, [_ for _ in range(4)])


def random_calculation(count):
    number = random.randint(20, 50)
    result = 0
    for i in range(number):
        result += i
        time.sleep(0.5)
    logging.info(result)

