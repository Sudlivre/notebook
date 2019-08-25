import re
from datetime import datetime


def utc2local(utc_dtm):
    # utc to local (+8:00)
    local_tm = datetime.fromtimestamp(0)
    utc_tm = datetime.utcfromtimestamp(0)
    offset = local_tm - utc_tm
    return utc_dtm + offset


def local2utc(local_dtm):
    # local to utc (-8:00)
    return datetime.utcfromtimestamp(local_dtm.timestamp())


def job2dict(job):
    job_repr = job.__repr__()
    job_str = job.__str__()
    id_name_str = re.search('id=(.*?) name=(.*?)\)', job_repr).groups()
    utc_next_run_time = re.search('next run at: (.*?) UTC', job_str).groups()[0]
    utc_time = datetime.strptime(utc_next_run_time, '%Y-%m-%d %H:%M:%S')
    local_time = utc2local(utc_time)
    next_run_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
    return dict(id=id_name_str[0], name=id_name_str[1], next_run_time=next_run_time)
