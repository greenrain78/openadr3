import json
from logging import getLogger
from logging.config import dictConfig

from ANN.ANNEngine import train, predict
from Controller.ScheduleManager import SchedulerManager

if __name__ == '__main__':
    # 로그 생성
    # with open('logs/loggers.json') as f:
    #     config = json.load(f)
    #     dictConfig(config)
    #
    # log = getLogger(__name__)
    # log.info('start main')
    #
    # schduler = SchedulerManager.init_schedule()

    # todo 작업 추가
    # 1주일
    # 15분
    train()
    predict()
