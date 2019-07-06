from nonebot import on_command, CommandSession

__plugin_name__ = '卖萌'
__plugin_usage__ = r"""
命令名称:卖萌
使用方法:喵一个
"""


@on_command('miao', aliases=['喵一个', '喵喵喵', '喵'])
async def miao(session: CommandSession):
    await session.send('喵~')
