from aiohttp import request
from complex_robot.secret import APP_SECRET, APP_KEY
from nonebot import on_command, CommandSession
import hashlib
import time
import uuid

__plugin_name__ = '翻译'
__plugin_usage__ = r"""
命令名称:翻译
使用方法:翻译 [翻译文本]
"""


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


@on_command('翻译')
async def traslation(session: CommandSession):
    YOUDAO_URL = 'http://openapi.youdao.com/api'
    data = {
        'q': truncate(session.current_arg_text),
        'from': 'auto',
        'to': 'auto',
        'appKey': APP_KEY,
        'salt': str(uuid.uuid1()),
        'signType': 'v3',
        'curtime': str(int(time.time()))
    }
    sign = encrypt(APP_KEY + data['q'] + data['salt'] + data['curtime'] + APP_SECRET)
    data['sign'] = sign
    async with request('POST', YOUDAO_URL, data=data) as resp:
        result = await resp.json()
        await session.send('翻译结果:' + result.get('translation', '')[0])
