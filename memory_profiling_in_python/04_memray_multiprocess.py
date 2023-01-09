from multiprocessing import Pool


def double(x: int) -> int:

    return x * 2


def main() -> None:

    Pool(4).map(double, range(10))


if __name__ == "__main__":

    main()
