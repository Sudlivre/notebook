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
