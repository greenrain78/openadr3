import json
from datetime import datetime
from logging import getLogger
from logging.config import dictConfig

from ANN.PredictEngine import run_predict
from Controller.ScheduleManager import run_schedule, create_schedule


def test_schedule():
    print(f"hello {datetime.now()}", flush=True)


if __name__ == '__main__':
    # 로그 생성
    # with open('logs/loggers.json') as f:
    #     config = json.load(f)
    #     dictConfig(config)
    #
    # log = getLogger(__name__)
    # log.info('start main')
    #
    # 데이터 가져오기


    # 데이터 저장


    test_schedule()
    create_schedule(test_schedule, "test hello", second=2)
    run_schedule()
    # schedulerM = SchedulerManager()
    #
    # schedulerM.create_schedule(run_train, "train", train_time)
    # schedulerM.create_schedule(run_predict, "train", train_time)

    # 15분
    # schedulerM.run_schedule()
    while True:
        pass

    print("end")