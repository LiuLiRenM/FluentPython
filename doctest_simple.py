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


def tuple_unpacking():
    """
    元组拆包

    >>> lax_coordinates = (33.9425, -118.408056)
    >>> latitude, longitude = lax_coordinates # 元组拆包
    >>> latitude
    33.9425
    >>> longitude
    -118.408056

    >>> divmod(20, 8)
    (2, 4)
    >>> t = (20, 8)
    >>> divmod(*t)
    (2, 4)
    >>> quotient, remainder = divmod(*t)
    >>> quotient, remainder
    (2, 4)

    >>> import os
    >>> _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
    >>> filename
    'idrsa.pub'

    >>> a, b, *rest = range(5)
    >>> a, b, rest
    (0, 1, [2, 3, 4])
    >>> a, b, *rest = range(3)
    >>> a, b, rest
    (0, 1, [2])
    >>> a, b, *rest = range(2)
    >>> a, b, rest
    (0, 1, [])
    """
    metro_areas = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
                   ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
                   ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
                   ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
                   ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)), ]
    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'
    for name, cc, pop, (lat, lon) in metro_areas:
        if lon <= 0:
            print(fmt.format(name, lat, lon))


if __name__ == '__main__':
    tuple_unpacking()
