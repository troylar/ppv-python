from dataclasses import dataclass
from datetime import date

from dateutil import rrule


@dataclass
class DateManager:
    start_date: date
    end_date: date
    start_of_week: int = 0

    def get_months(self):
        return list(
            rrule.rrule(
                rrule.MONTHLY,
                bymonthday=1,
                dtstart=self.start_date,
                until=self.end_date,
            )
        )

    def get_weeks(self):
        return list(
            rrule.rrule(
                rrule.WEEKLY,
                byweekday=self.start_of_week,
                dtstart=self.start_date,
                until=self.end_date,
            )
        )

    def get_days(self):
        return list(
            rrule.rrule(
                rrule.DAILY,
                dtstart=self.start_date,
                until=self.end_date,
            )
        )
