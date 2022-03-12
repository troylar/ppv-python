import unittest

import arrow

from dates import DateManager


class TestDateManager(unittest.TestCase):
    def test_can_initialize_start_date(self):
        test_date = arrow.get("2022-03-15")
        dm = DateManager(start_date=test_date, end_date=arrow.get("2022-03-30"))
        assert dm.start_date == test_date

    def test_can_initialize_end_date(self):
        test_date = arrow.get("2022-03-15")
        dm = DateManager(start_date=arrow.get("2022-03-01"), end_date=test_date)
        assert dm.end_date == test_date

    def test_can_get_months(self):
        dm = DateManager(
            start_date=arrow.get("2022-03-01"), end_date=arrow.get("2022-03-30")
        )
        assert len(dm.get_months()) == 1

    def test_can_get_weeks(self):
        dm = DateManager(
            start_date=arrow.get("2022-03-01"), end_date=arrow.get("2022-03-30")
        )
        assert len(dm.get_weeks()) == 4

    def test_can_get_days(self):
        dm = DateManager(
            start_date=arrow.get("2022-03-01"), end_date=arrow.get("2022-03-30")
        )
        assert len(dm.get_days()) == 30
