import unittest

from DataAdapter.DataReceiver import DataReceiver


class DataReceiverTest(unittest.TestCase):

    def test_runs_check_api_eqps(self):
        """단순 실행여부 판별하는 테스트 메소드"""
        test_api = DataReceiver()
        data = test_api.check_api_eqps('ace')
        print("check_api_eqps")
        print(data)

    def test_runs_check_api_elec(self):
        """단순 실행여부 판별하는 테스트 메소드"""
        pass


test_api = DataReceiver()
data = test_api.check_api_elec('ace', 300, 20210309)
print("check_api_elec")
print(data)
