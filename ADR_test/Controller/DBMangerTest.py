import unittest

from Controller.DBManger import runSQL


class DBManagerTest(unittest.TestCase):

    def test_runs(self):
        """단순 실행여부 판별하는 테스트 메소드"""
        runSQL("select * from")


