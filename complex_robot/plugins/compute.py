from nonebot import on_command, CommandSession
from math import *


@on_command('compute', aliases=['计算'])
async def weather(session: CommandSession):
    try:
        await session.send(str(eval(session.current_arg_text.strip())))
    except:
        await session.send('计算出错')
