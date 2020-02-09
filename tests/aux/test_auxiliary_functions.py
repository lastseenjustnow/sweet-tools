from unittest import TestCase

from aux.auxiliary_functions import daterange_delta89
from datetime import timedelta, date, datetime


class TestDateRangeDelta89(TestCase):
    start_date = date(2010, 1, 1)
    end_date = date(2020, 1, 1)
    dates = []
    for single_date in daterange_delta89(start_date, end_date):
        dates.append(single_date.strftime("%d/%m/%Y"))

    print(dates)
