from nonebot import on_command, CommandSession
from aiohttp import request

__plugin_name__ = '新番导视'
__plugin_usage__ = r"""
命令名称:新番导视
使用方法:新番导视
"""


@on_command('新番导视')
async def bilibili(session: CommandSession):
    anime = []
    async with request('GET', 'https://bangumi.bilibili.com/media/web_api/search/result?season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&pub_date=-1&style_id=-1&order=0&st=1&sort=0&page=1&season_type=1&pagesize=20') as resp:
        data = await resp.json()
        for text in data['result']['data']:
            if '僅限' not in text['title']:
                anime.append(text['title'])
        await session.send('\n'.join(anime))
