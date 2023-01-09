import threading

import time


def expensive_operation(delay: int) -> None:

    time.sleep(delay)
    print("hw")


def main() -> None:

    threads = [
        threading.Thread(target=expensive_operation, args=(delay,))
        for delay in range(1, 4)
    ]
    for _ in map(lambda x: x.start(), threads): pass
    for _ in map(lambda x: x.join(), threads): pass


if __name__ == "__main__":

    main()
