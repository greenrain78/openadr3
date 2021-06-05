"""
Schedule DB SchedulerManager
실질적인 스캐줄 객체
"""
import logging

from apscheduler.schedulers.background import BackgroundScheduler

log = logging.getLogger(__name__)

# 스캐줄 생성
schedule = BackgroundScheduler()
log.debug("SchedulerManager init schedule")


def create_schedule(method, schedule_id: str, **schedule_time):
    """
    :param method: 실행할 함수
    :param schedule_id: 스캐줄 id
    :param schedule_time: 반복할 시간
    :return:
    """
    schedule.add_job(method, 'cron', id=schedule_id, **schedule_time)


def delete_schedule(schedule_id: str):
    schedule.resume_job(schedule_id)


def run_schedule():
    schedule.start()
