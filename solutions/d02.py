import os
import pathlib
import pandas as pd


def read_input(file: str) -> list:
    df = pd.read_csv(file, sep="\\s+", header=None)
    data = df.values.tolist()
    return data

def p1(reports: list[list]) -> int:
    for report in reports:
        if (
            report == sorted(report)
            or report == sorted(report, reverse=True)
        ):
            safe = True
        else:
            safe = False
        prev_level = None
        prev_diff = 0
        for idx, level in enumerate(report):
            if idx == 0:
                prev = level
            else:
                if abs(prev_level - level) >= 3:
                    safe = False
                    break
                elif
                diff = prev_level - level
                if 

    pass


def p2(left: list, right: list) -> int:
    pass


def main():

    file = os.path.join(pathlib.Path(__file__).parent.resolve(), "../input", "d02s.txt")
    data = read_input(file)
    print(data)

    # p1_score = p1()
    # print(f"Part 1 score: {p1_score}")

    # p2_score = p2()
    # print(f"Part 2 score: {p2_score}")


if __name__ == "__main__":
    main()
