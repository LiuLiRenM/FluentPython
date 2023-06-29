"""
《流畅的python》第二版
第三章第二节 例子集合

"""


def dict_derivation_example():
    """
    一个字典推导式的示例：根据同一个元组列表构建两个字典（附带doctest的测试用例）

    >>> dial_codes = [
    ...    (86, 'China'),
    ...    (91, 'India'),
    ...    (1, 'United States'),
    ...    (62, 'Indonesia'),
    ...    (55, 'Brazil'),
    ...    (92, 'Pakistan'),
    ...    (880, 'Bangladesh'),
    ...    (234, 'Nigeria'),
    ...    (7, 'Russia'),
    ...    (81, 'Japan'),
    ...    ]
    >>> country_dial = {country: code for code, country in dial_codes}
    >>> country_dial
    {'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62, 'Brazil': 55, 'Pakistan': 92, 'Bangladesh': 880, 'Nigeria': 234, 'Russia': 7, 'Japan': 81}
    >>> {code: country.upper() for country, code in sorted(country_dial.items()) if code < 70}
    {55: 'BRAZIL', 62: 'INDONESIA', 7: 'RUSSIA', 1: 'UNITED STATES'}
    """
    dial_codes_1 = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]
    country_dial_1 = {country: code for code, country in dial_codes_1}
    print(country_dial_1)
    filter_country_dial = {code: country.upper() for country, code in sorted(country_dial_1.items()) if code < 70}
    print(filter_country_dial)


def unpack():
    """
    演示映射拆包（附带doctest的测试用例）

    >>> def dump(**kwargs):
    ...     return kwargs
    ...
    >>> dump(**{'x': 1}, y=2, **{'z': 3})
    {'x': 1, 'y': 2, 'z': 3}
    >>> {'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}}
    {'a': 0, 'x': 4, 'y': 2, 'z': 3}
    """

    def dump_1(**kwargs):
        return kwargs

    print(dump_1(**{'x': 1}, y=2, **{'z': 3}))


def merge_mapping():
    """
    使用|和|=进行合并映射操作（附带doctest的测试用例）

    >>> d11 = {'a': 1, 'b': 2}
    >>> d22 = {'a': 2, 'b': 4, 'c': 6}
    >>> d11 | d22
    {'a': 2, 'b': 4, 'c': 6}
    >>> d11
    {'a': 1, 'b': 2}
    >>> d11 |= d22
    >>> d11
    {'a': 2, 'b': 4, 'c': 6}
    """
    d1 = {'a': 1, 'b': 2}
    d2 = {'a': 2, 'b': 4, 'c': 6}
    result = d1 | d2
    print(d1)
    print(d2)
    print(result)
    d1 |= d2
    print(d1)


if __name__ == '__main__':
    # dict_derivation_example()
    # unpack()
    merge_mapping()
