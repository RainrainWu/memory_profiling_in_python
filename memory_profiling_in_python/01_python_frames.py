import inspect

from memory_profiling_in_python._helpers import view_frames


def get_stack(x: int) -> None:

    view_frames(inspect.stack(context=4))


def main() -> None:

    get_stack(1+1)


if __name__ == "__main__":

    main()
