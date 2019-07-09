from nonebot import on_command, CommandSession


@on_command('run', aliases=['运行代码'])
async def run(session: CommandSession):
    text = session.current_arg_text.split(maxsplit=1)
    language = text[0]
    if language.lower() == 'python':
        file = r'python\code.py'
    elif language.lower() == 'c++' or language == 'cpp':
        file = r'cpp\code.cpp'
    elif language.lower() == 'c':
        file = r'c\code.c'
    elif language.lower() == 'c#':
        file = r'csharp\code.cs'
    elif language.lower() == 'java':
        file = r'java\code.java'
    else:
        await session.send('暂不支持该语言')
        return
    code = open(file, 'w', encoding='utf-8')
    code.write(text[1])
    code.close()