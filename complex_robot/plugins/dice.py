from nonebot import on_command, CommandSession
import random


@on_command('dice', aliases=['掷骰子'])
async def dice(session: CommandSession):
    await session.send(str(random.randint(1, 7)))
