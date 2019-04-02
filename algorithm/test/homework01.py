import threading
from functools import wraps
import requests


# 单例模式
class Singleton:
    """
    单利模式
    """
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


def conn_try_again(func):
    """
    网络请求重试装饰器
    """
    retries = 0
    count = {"num": retries}
    # 让func能够传参
    @wraps(func)
    def wrapped(*arges, **kwarges):
        try:
            return func(*arges, **kwarges)
        except Exception:
            if count['num'] < 2:
                count['num'] += 1
                print('retries times:', count['num'])
                return wrapped(*arges, **kwarges)
    return wrapped


@conn_try_again
def get_page(url):
    """
    网络请求
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

get_page('https:www.baidu.comm')
