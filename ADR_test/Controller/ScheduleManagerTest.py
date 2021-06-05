import unittest
from datetime import datetime

from Controller.ScheduleManager import run_schedule, create_schedule


def test_schedule():
    print(f"hello {datetime.now()}", flush=True)


class ScheduleManagerTest(unittest.TestCase):

    def test_runs(self):
        """단순 실행여부 판별하는 테스트 메소드"""
        create_schedule(test_schedule, "test hello", second=2)
        run_schedule()


