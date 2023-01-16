def foo(n):
    x = []
    for _ in range(n):
        x.append(None)
    return x

foo(1_000_000)


def bar(n):
    return [None] * n

bar(1_000_000)
