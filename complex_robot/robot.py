from complex_robot import config
import nonebot
import os

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        os.path.join(os.path.dirname(__file__), 'plugins'),
        'complex_robot.plugins')
    nonebot.run()
