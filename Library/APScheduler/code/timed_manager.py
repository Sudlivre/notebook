from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from pymongo import MongoClient


def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@singleton
class TimedTaskManager(object):
    def __init__(self):
        self.mongo_client = MongoClient()
        self.jobstores = {
            'default': MongoDBJobStore(client=self.mongo_client),
            # 'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
        }
        self.executors = {
            # 'default': ThreadPoolExecutor(20),
            'default': ProcessPoolExecutor(5)
        }
        self.job_defaults = {
            'coalesce': False,
            'max_instances': 1
        }
        self.scheduler = BackgroundScheduler(jobstores=self.jobstores,
                                             executors=self.executors,
                                             job_defaults=self.job_defaults,
                                             timezone=utc)

    def add_default_job(self, func):
        return self.scheduler.add_job(func)

    def add_cron_job(self, func, *args, **kwargs):
        year = kwargs.get('year', '*')
        month = kwargs.get('month', '*')
        day = kwargs.get('day', '*')
        hour = kwargs.get('hour', '*')
        minute = kwargs.get('minute', '*')
        second = kwargs.get('second', 20)
        return self.scheduler.add_job(func, trigger='cron',
                               year=year, month=month,
                               day=day, hour=hour,
                               minute=minute, second=second)

    def get_jobs(self):
        return self.scheduler.get_jobs()

    def get_all_jobs_from_mongo(self):
        """
        :return:
        [<Job (id=task_id name=task_name)>]
        [<class 'apscheduler.job.Job'>]
        """
        return self.jobstores.get('default').get_all_jobs()

    def start_scheduler(self):
        self.scheduler.start()

    def shutdown_scheduler(self):
        self.scheduler.shutdown(wait=False)
