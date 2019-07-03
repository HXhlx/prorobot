from nonebot import on_command, CommandSession, permission, CQHttpError, on_request, RequestSession


@on_command('miao', aliases=['喵一个', '喵喵喵', '喵'])
async def miao(session: CommandSession):
    await session.send('喵~')


@on_command('get_member_count', aliases=['总人数'], permission=permission.GROUP_ADMIN, only_to_me=False)
async def count(session: CommandSession):
    group_id = session.ctx['group_id']
    try:
        member_list = await session.bot.get_group_member_list(group_id=group_id)
    except CQHttpError:
        await session.send('无法获取')
        return
    await session.send(f'群里一共有{len(member_list)}个人')


@on_request('friend', 'group')
async def _(session: RequestSession):
    await session.approve()
    await session.reject()
