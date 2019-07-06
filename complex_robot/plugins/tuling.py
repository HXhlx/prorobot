from aiocqhttp.message import escape
from typing import Optional
from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand
from nonebot.helpers import context_id, render_expression
import json
import aiohttp

__plugin_name__ = '智能聊天'
__plugin_usage = r"""
命令名称:智能聊天
使用方法:直接跟我聊天即可~
""".strip()
EXPR_DONT_UNDERSTAND = (
    '我现在还不太明白你在说什么呢，但没关系，以后的我会变得更强呢！',
    '我有点看不懂你的意思呀，可以跟我聊些简单的话题嘛',
    '其实我不太明白你的意思……',
    '抱歉哦，我现在的能力还不能够明白你在说什么，但我会加油的～'
)


@on_command('tuling')
async def tuling(session: CommandSession):
    message = session.state.get('message')
    reply = await call_tuling_api(session, message)
    if reply:
        await session.send(escape(reply))
    else:
        await session.send(render_expression(EXPR_DONT_UNDERSTAND))


@on_natural_language
async def _(session: NLPSession):
    return IntentCommand(60.0, 'tuling', args={'message': session.msg_text})


async def call_tuling_api(session: CommandSession, text: str) -> Optional[str]:
    if not text:
        return None
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    payload = {
        'reqType': 0,
        'perception': {
            'inputText': {
                'text': text
            }
        },
        'userInfo': {
            'apiKey': session.bot.config.TULING_API_KEY,
            'userId': context_id(session.ctx, use_hash=True)
        }
    }
    group_unique_id = context_id(session.ctx, mode='group', use_hash=True)
    if group_unique_id:
        payload['userInfo']['groupId'] = group_unique_id
    try:
        async with aiohttp.ClientSession() as sess:
            async with sess.post(url, json=payload) as response:
                if response.status != 200:
                    return None
                resp_payload = json.loads(await response.text())
                if resp_payload['results']:
                    for result in resp_payload['results']:
                        if result['resultType'] == 'text':
                            return result['values']['text']
    except (aiohttp.ClientError, json.JSONDecodeError, KeyError):
        return None
