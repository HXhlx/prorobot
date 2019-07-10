from nonebot import RequestSession, on_request, get_bot


@on_request('friend')
async def friends(session: RequestSession):
    await session.approve()
    text = '''你好,我是Trobot,是HX制作的功能性机器人,很高兴认识你!
开发者QQ:HX,1367557521
github地址:https://github.com/HXhlx/prorobot'''
    bot = get_bot()
    await bot.send_private_msg(user_id=session.ctx['user_id'], message=text)
