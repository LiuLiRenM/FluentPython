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


def listcomps():
    """
    列表推导

    >>> symbols = '$¢£¥€¤'
    >>> codes = []
    >>> for symbol in symbols:
    ...     codes.append(ord(symbol))
    ...
    >>> codes
    [36, 162, 163, 165, 8364, 164]

    >>> symbols = '$¢£¥€¤'
    >>> codes = [ord(symbol) for symbol in symbols]
    >>> codes
    [36, 162, 163, 165, 8364, 164]

    >>> symbols = '$¢£¥€¤'
    >>> beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    >>> beyond_ascii
    [162, 163, 165, 8364, 164]
    >>> beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
    >>> beyond_ascii
    [162, 163, 165, 8364, 164]

    """
    pass


def cartesian_product():
    """
    笛卡尔积

    >>> colors = ['black', 'white']
    >>> sizes = ['S', 'M', 'L']
    >>> t_shirts = [(color, size) for color in colors for size in sizes]
    >>> t_shirts
    [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]

    >>> for color in colors:
    ...     for size in sizes:
    ...         print((color, size))
    ('black', 'S')
    ('black', 'M')
    ('black', 'L')
    ('white', 'S')
    ('white', 'M')
    ('white', 'L')

    >>> t_shirts = [(color, size) for size in sizes for color in colors]
    >>> t_shirts
    [('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'), ('black', 'L'), ('white', 'L')]

    """
    pass


def genexps():
    """
    生成器表达式

    >>> symbols = '$¢£¥€¤'
    >>> tuple(ord(symbol) for symbol in symbols)
    (36, 162, 163, 165, 8364, 164)

    >>> import array
    >>> array.array('I', (ord(symbol) for symbol in symbols))
    array('I', [36, 162, 163, 165, 8364, 164])

    >>> colors = ['black', 'white']
    >>> sizes = ['S', 'M', 'L']
    >>> for t_shirt in ('%s %s'%(c, s) for c in colors for s in sizes):
    ...     print(t_shirt)
    ...
    black S
    black M
    black L
    white S
    white M
    white L
    """
    pass
