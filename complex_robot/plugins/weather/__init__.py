from .data_source import get_weather_of_city
from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from jieba import posseg

__plugin_name__ = '天气'
__plugin_usage__ = r"""
命令名称:天气查询
使用方法:天气 [城市名称]
"""


@on_command('weather', aliases=['天气', '查天气'])
async def weather(session: CommandSession):
    city = session.get('city', prompt='你想查询哪个城市的天气呢？')
    weather_report = await get_weather_of_city(city)
    await session.send(weather_report)


@weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('要查询的城市名称不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg


@on_natural_language(keywords={'天气'})
async def _(session: NLPSession):
    stripped_msg = session.msg_text.strip()
    words = posseg.lcut(stripped_msg)
    city = None
    for word in words:
        if word.flag == 'ns':
            city = word.word
    return IntentCommand(90, 'weather', current_arg=city or '')
