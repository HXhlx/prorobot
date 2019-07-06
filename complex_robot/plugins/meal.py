from nonebot import on_command, CommandSession
from bs4 import BeautifulSoup
import aiohttp
import random

__plugin_name__ = '吃什么'
__plugin_usage__ = r"""
命令名称:吃什么
使用方法:早上吃什么 中午吃什么 晚上吃什么
"""


@on_command('meal', aliases=['早上吃什么', '中午吃什么', '晚上吃什么'])
async def meal(session: CommandSession):
    async with aiohttp.request('GET', 'http://www.chinacaipu.com/', headers={"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"}) as response:
        soup = BeautifulSoup(await response.text())
        tag = soup.find(class_='i_bg2')
        tags = tag.find_all('strong')
        m = random.choice(tags[1:])
        await session.send(m.get_text())
