"""
《流畅的python》第二版 19章第四节的第一个例子
使用线程实现旋转指针

"""
import itertools
import time
from threading import Event, Thread


def spin(msg: str, done: Event) -> None:
    status = ''
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        # 设置了时间之后，程序会阻塞在这个方法上面，就不会向终端打印字符，以达到动画效果
        # 0.1秒之后done.wait()返回False，然后程序继续打印字符
        if done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


def slow() -> int:
    time.sleep(13)
    return 42


def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=('thinking', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')


if __name__ == '__main__':
    main()
