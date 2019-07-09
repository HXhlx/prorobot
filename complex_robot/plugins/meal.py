from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from bs4 import BeautifulSoup
import aiohttp
import random

__plugin_name__ = '吃什么'
__plugin_usage__ = r"""
命令名称:吃什么
使用方法:吃什么 吃啥
"""


@on_command('meal', aliases=['吃什么', '吃啥'])
async def meal(session: CommandSession):
    async with aiohttp.request('GET', 'http://www.chinacaipu.com/', headers={"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"}) as response:
        soup = BeautifulSoup(await response.text())
        tag = soup.find(class_='i_bg2')
        tags = tag.find_all('strong')
        m = random.choice(tags[1:])
        await session.send(m.get_text())


@on_natural_language(keywords={'吃什么', '吃啥'})
async def _(session: NLPSession):
    return IntentCommand(90, 'meal')
