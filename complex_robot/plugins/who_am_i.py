from nonebot import on_command, CommandSession

__plugin_name__ = '我是谁'
__plugin_usage__ = r"""
命令名称:我是谁
使用方法:我是谁
"""


@on_command('who_am_i', aliases=['我是谁'])
async def who(session: CommandSession):
    await session.send('你是' + str(session.ctx['sender']['nickname']) + '\n帐号:' + str(session.ctx['user_id']))
