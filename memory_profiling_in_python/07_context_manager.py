from memray import Tracker, FileDestination


def foo(n):
    x = []
    for _ in range(n):
        x.append(None)
    return x

with Tracker(
    destination=FileDestination(
        "memray.bin",
        overwrite=True,
    )
):

    foo(1_000_000)
