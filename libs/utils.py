# python level imports
import datetime

# project level imports
from .constants import INVALID_QUERY_PARAMS

def next_day_occurence(current_date, weekday):
    """
    This function returns the next date a day will occur.
    """
    assert isinstance(current_date, datetime.date), "current_date should be a date object"
    assert isinstance(weekday, int), "weekday should be int object"
    days_ahead = weekday - current_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return current_date + datetime.timedelta(days_ahead)


def increment_hour(time, inc=1):
    """
    This function increments the time object by 1 hour
    """
    assert isinstance(time, datetime.time), "time should be a datetime.time object"
    return time.replace(hour=time.hour + inc)


def apply_query_params(qs, query_params, fields):
    """
    This function applies the query_params in url to a queryset
    and returns the queryset.
    """
    assert isinstance(query_params, dict), "query_params should be dict object"
    assert isinstance(fields, list), "fields should be list object"

    msg = None
    if len(query_params) == 0:
        pass
    else:
        for param, value in query_params.items():
            param = param.split('__')
            # changing param to support related model lookups
            param = param[0] + '__' + param[1] if len(param) > 1 else param[0]
            # allowing filtering only on given fields
            if param in fields:
                try:
                    qs = qs.filter(**{param: value[0]})
                except Exception:
                    msg = INVALID_QUERY_PARAMS
                    break
    return qs, msg
