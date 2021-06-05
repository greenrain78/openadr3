from datetime import datetime
from logging import getLogger

from settings import is_test_data

log = getLogger(__name__)


def read_data(siteId, perfId, api_time="now"):
    """
    데이터를 읽어 온다
    :param perfId:
    :param siteId:
    :param api_time: api를 통해 받아올 데이터의 날짜
    :return:
    """
    # 테스트 데이터를 사용하여 데이터를 읽어오기
    if is_test_data:
        data = read_test_data()
        return data
    else:
        data = read_api_data(api_time)
        return data


def read_api_data(siteId, perfId, api_time):
    """
    """
    # 오늘 날짜 기준으로 데이터를 받음
    if api_time == "now":
        req_time = datetime.now().strftime("%Y%m%d")  # 오늘 날짜를 api 형식에 맞게 변형
        log.debug(f"api 데이터 수집: {req_time}")
        data = check_api_elec()
        return data
        pass
    else:
        log.error("api 요청 날짜가 잘못 설정")





def read_test_data():
    pass
