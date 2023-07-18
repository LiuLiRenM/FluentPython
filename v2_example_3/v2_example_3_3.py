"""
《流畅的python》第二版
第三章第三节-使用模式匹配处理映射 例子集合

"""


def get_creators(record: dict) -> list:
    """
    从出版物记录中提取创作者的名字

    >>> b1 = dict(api=1, author='Douglas Hofstadter',
    ...         type='book', title='Gödel, Escher, Bach')
    >>> get_creators(b1)
    ['Douglas Hofstadter']
    >>> from collections import OrderedDict
    >>> b2 = OrderedDict(api=2, type='book',
    ...         title='Python in a Nutshell',
    ...         authors='Martelli Ravenscroft Holden'.split())
    >>> get_creators(b2)
    ['Martelli', 'Ravenscroft', 'Holden']
    >>> get_creators({'type': 'book', 'pages': 770})
    Traceback (most recent call last):
        ...
    ValueError: Invalid "book" record: {'type': 'book', 'pages': 770}

    >>> get_creators('Spam, spam, spam')
    Traceback (most recent call last):
        ...
    ValueError: Invalid record: 'Spam, spam, spam'

    :param record: 出版物记录
    :return: 创作者的名字
    """
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f'Invalid "book" record: {record!r}')
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')


if __name__ == '__main__':
    get_creators('Spam, spam, spam')
