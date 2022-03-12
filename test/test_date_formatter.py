import unittest

import arrow

from dates import DateFormatter


class TestDateFormatter(unittest.TestCase):
    def test_can_format_month_title(self):
        assert DateFormatter.to_month_title(arrow.get("2022-03-01")) == "Mar '22"

    def test_can_format_week_title(self):
        assert (
            DateFormatter.to_week_title("2022-03-01", "2022-03-06") == "Mar 01 - Mar 06"
        )
