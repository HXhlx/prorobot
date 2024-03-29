from nonebot import on_command, CommandSession
import nonebot


@on_command('usage', aliases=['使用帮助', '帮助', "使用方法"])
async def usage(session: CommandSession):
    plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))
    arg = session.current_arg_text.strip().lower()
    if not arg:
        await session.send('我现在支持的功能有:\n' + '\n'.join(p.name for p in plugins))
        return
    for p in plugins:
        if p.name.lower() == arg:
            await session.send(p.usage)
