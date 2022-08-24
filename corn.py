from apscheduler.schedulers.blocking import BlockingScheduler

from smtp import stmp

class corn:
    def start_corn_task(self):
        scheduler = BlockingScheduler()
        scheduler.add_job(stmp().task_strategy01_corn, 'cron', hour=13, minute=30)
        scheduler.add_job(stmp().task_strategy02_corn, 'cron', hour='9-10', minute='*/1')#9点到10点每分钟触发一次
        try:
            scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass