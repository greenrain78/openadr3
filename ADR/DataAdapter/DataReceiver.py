from typing import Optional

import requests


class DataReceiver(object):
    """
    open adr api 테스트
    """
    BASE_URL = 'http://222.122.224.225:9091/cems-api'
    version: Optional[str] = None

    def __init__(self, version: str = 'v1.0'):
        self.version = version

    @property
    def api_url(self) -> str:
        return f'{self.BASE_URL}/{self.version}'

    @property
    def header_data(self) -> dict:
        return {
            'Authorization': '1234qwer',
        }

    def check_api_eqps(self, siteId: str):
        """
        :param siteId:
        :return:
        """
        url = f'{self.api_url}/ems/eqps/{siteId}'
        response = requests.get(url, headers=self.header_data)
        json_resp = response.json()

        return json_resp.get("data", [])

    def check_api_elec(self, siteId: str, perfId, ymd):
        """
        :param siteId:
        :param perfId:
        :param ymd:
        :return:
        - pnName     : 판넬명
        - eqpName    : 설비명
        - perfId        : 성능 ID
        - ymdms       : 일시
        - amPere       : 전류
        - arPower      : 피상전력
        - atvPower     : 유효전력
        - ratPower      : 무효전력
        - pwFactor      : 역률
        - accruePower  : 누적전력량
        - voltagerS      : RS선간전압
        - voltagesT      : ST선간전압
        - voltagetR      : TR선간전압
        - temperature   :온도
        """
        url = f'{self.api_url}/ems/elec/{siteId}/{perfId}/{ymd}'
        response = requests.get(url, headers=self.header_data)
        json_resp = response.json()
        print(url)
        print(response)
        return json_resp.get("data", [])

