"""
loguru框架的使用案例

"""
from loguru import logger

logger.add('logs/fluent_python.log', serialize=True)


def loguru_try():
    """
    尝试loguru的输出json功能

    """
    logger.info(f'hi, i am loguru.')


if __name__ == '__main__':
    loguru_try()
