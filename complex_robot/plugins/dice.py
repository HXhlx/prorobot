from nonebot import on_command, CommandSession
import random

__plugin_name__ = '掷骰子'
__plugin_usage__ = r"""
命令名称:掷骰子
使用方法:掷骰子
"""


@on_command('dice', aliases=['掷骰子'])
async def dice(session: CommandSession):
    await session.send(str(random.randint(1, 7)))
