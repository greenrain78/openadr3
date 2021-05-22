"""
Schedule DB SchedulerManager
실질적인 스캐줄 객체
"""
import logging

from apscheduler.schedulers.background import BackgroundScheduler

log = logging.getLogger(__name__)


class SchedulerManager:
    log.info("SchedulerManager init schedule")

    @classmethod
    def init_schedule(cls):
        # 스캐줄 생성
        cls.schedule = BackgroundScheduler()
        log.info("SchedulerManager init schedule")
        return cls.schedule

    @classmethod
    def get_schedule(cls) -> BackgroundScheduler:
        return cls.schedule

    @classmethod
    def create_schedule(cls, method, schedule_id: str, hour: int, minutes: int, seconds: int):
        cls.schedule.add_job(method, 'cron', hour=hour, minutes=minutes, seconds=seconds, id=schedule_id)

    @classmethod
    def delete_schedule(cls, schedule_id: str):
        cls.schedule.resume_job(schedule_id)


