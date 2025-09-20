# -*- coding: utf-8 -*-


def diff(iterable):
    a, b = iterable
    return a - b

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        print(
            sum(
                map(
                    abs,
                    map(
                        diff,
                        zip(
                            *(
                                map(
                                    sorted,
                                    map(
                                        list,
                                        zip(*(map(int, line.split()) for line in f)),
                                    ),
                                )
                            )
                        ),
                    ),
                )
            )
        )
