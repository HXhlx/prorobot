from nonebot import RequestSession, permission, CQHttpError, on_request, on_command, CommandSession, on_notice, NoticeSession

__plugin_name__ = '计算总人数(群专用)'
__plugin_usage__ = r"""
命令名称:总人数
使用方法:总人数
"""


@on_command('get_member_count', aliases=['总人数'], permission=permission.GROUP_ADMIN, only_to_me=False)
async def count(session: CommandSession):
    group_id = session.ctx['group_id']
    try:
        member_list = await session.bot.get_group_member_list(group_id=group_id)
        await session.send(f'群里一共有{len(member_list)}个人')
    except CQHttpError:
        await session.send('无法获取')


@on_request('group')
async def group(session: RequestSession):
    if session.ctx['comment'] == '暗号':
        await session.approve()
    else:
        await session.reject('请说暗号')


@on_notice('group_increase')
async def welcome(session: NoticeSession):
    await session.send('欢迎新朋友~')
