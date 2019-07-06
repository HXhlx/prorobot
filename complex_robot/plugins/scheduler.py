from datetime import datetime
from aiocqhttp.exceptions import Error
import nonebot
import pytz

__plugin_name__ = '定点报时(禁用中)'
__plugin_usage__ = r"""
命令名称:定点报时
使用方法:群内自动调用
"""


@nonebot.scheduler.scheduled_job('cron', hour='*')
async def scheduler():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=0000000, message=f'现在{now.hour}点整啦!')
    except Error:
        pass
