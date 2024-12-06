import os
import pathlib
import pandas as pd


def read_input(file: str) -> list:
    # df = pd.read_csv(file, sep="\\s+", header=None)
    # data = df.values.tolist()
    # return data
    reports = []
    with open(file) as f:
        for l in f.readlines():
            report = [int(x) for x in l.split()]
            reports.append(report)
    return reports


def always_increase_decrease(report:list) -> bool:
    if (
        report != sorted(report)
        and report != sorted(report, reverse=True)
    ):
        print(f"Unsafe. Level not always decreasing/increasing {report}")
        return False
    else:
        return True


def p2_fails_increase_decrease(report:list) -> bool:
    increases = []
    for idx, level in enumerate(report):
        if idx == 0:
            prev_level = level
        else:
            increases.append(prev_level < level)
    # If majority of changes are increases flip Trues to failed increases
    if sum(increases) < len(increases) / 2:
        fails = [not x for x in increases]
    else:
        # Majority decreases so fails are increases
        fails = increases
    return fails


def within_distance(report:list, dist:int) -> bool:
    for idx, level in enumerate(report):
        if idx == 0:
            prev_level = level
        else:
            change = abs(prev_level - level)
            if change == 0 or change > dist:
                print(f"Unsafe. Level difference too much {report}")
                return False
            else:
                prev_level = level
    return True


def p2_fail_distance(report:list, dist:int) -> bool:
    fails = []
    for idx, level in enumerate(report):
        if idx == 0:
            prev_level = level
        else:
            change = abs(prev_level - level)
            fails.append(
                (change == 0 or change > dist)
            )
            prev_level = level
    return fails


def p1(reports: list[list]) -> int:
    safe_reports = []
    for idx, report in enumerate(reports):
        safe = always_increase_decrease(report)
        if safe:
            safe = within_distance(report, 3)
        safe_reports.append(safe)
    return sum(safe_reports)


def p2(left: list, right: list) -> int:
    pass


def main():

    file = os.path.join(pathlib.Path(__file__).parent.resolve(), "../input", "d02.txt")
    data = read_input(file)

    p1_score = p1(data)
    print(f"Part 1 safe reports: {p1_score}")

    # p2_score = p2()
    # print(f"Part 2 score: {p2_score}")


if __name__ == "__main__":
    main()
