from nonebot import on_command, CommandSession
from bs4 import BeautifulSoup
import requests
import random


@on_command('meal', aliases=['早上吃什么', '中午吃什么', '晚上吃什么'])
async def meal(session: CommandSession):
    response = requests.get('http://www.chinacaipu.com/', headers={"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"})
    print(response)
    soup = BeautifulSoup(response.text)
    tag = soup.find(class_='i_bg2')
    tags = tag.find_all('strong')
    m = random.choice(tags[1:])
    await session.send(m.get_text())
