from nonebot import on_command, CommandSession


@on_command('who_am_i', aliases=['我是谁'])
async def who(session: CommandSession):
    await session.send('你是' + str(session.ctx['sender']['nickname']) + '\n帐号:' + str(session.ctx['user_id']))
