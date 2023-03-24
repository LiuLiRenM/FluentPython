"""
doctest框架的使用案例

"""


def my_function(a, b):
    """
    >>> my_function(2, 3)
    6
    >>> my_function('a', 3)
    'aaa'

    :param a: 参数a
    :param b: 参数b
    :return: a * b 的结果
    """
    return a * b


def my_function_another(a, b):
    """
    Returns a * b
    Works with numbers:

    >>> my_function(2, 3)
    6

    and strings:

    >>> my_function('a', 3)
    'aaa'

    :param a:
    :param b:
    :return:
    """
    return a * b
