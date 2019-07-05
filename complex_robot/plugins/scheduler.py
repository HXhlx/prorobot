from datetime import datetime
from aiocqhttp.exceptions import Error
import nonebot
import pytz


@nonebot.scheduler.scheduled_job('cron', hour='*')
async def _scheduler():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=0000000, message=f'现在{now.hour}点整啦!')
    except Error:
        pass
