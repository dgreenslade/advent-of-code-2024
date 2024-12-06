import os
import pathlib


def read_input(file: str) -> list:
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
        # print(f"Unsafe. Level not always decreasing/increasing {report}")
        return False
    else:
        return True


def within_distance(report:list, dist:int) -> bool:
    for idx, level in enumerate(report):
        if idx == 0:
            prev_level = level
        else:
            change = abs(prev_level - level)
            if change == 0 or change > dist:
                # print(f"Unsafe. Level difference too much {report}")
                return False
            else:
                prev_level = level
    return True


def p1(reports: list[list]) -> int:
    safe_reports = []
    for report in reports:
        safe = always_increase_decrease(report)
        if safe:
            safe = within_distance(report, 3)
        safe_reports.append(safe)
    return sum(safe_reports)


def safe(report:list) -> bool:
    """Combine two conditions of report being safe by using sets"""
    pos_steps = set([1, 2, 3])
    neg_steps = set([-1, -2, -3])
    level_steps = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    return any([
        set(level_steps) - pos_steps == set(),
        set(level_steps) - neg_steps == set()
    ])


def p1_sets(reports: list[list]) -> int:
    """Redo part 1 with different method of finding safe"""
    safe_reports = [safe(r) for r in reports]
    return sum(safe_reports)


def p2(reports: list) -> int:
    safe_reports = []
    for r in reports:
        modified = []
        for i in range(len(r)):
            # remove one level from report
            modified.append(r[:i] + r[i+1:])
        safe_reports.append(any([safe(m) for m in modified]))
    return sum(safe_reports)


def main():

    file = os.path.join(pathlib.Path(__file__).parent.resolve(), "../input", "d02.txt")
    data = read_input(file)

    p1_score = p1(data)
    print(f"Part 1 score: {p1_score}")

    p2_score = p2(data)
    print(f"Part 2 score: {p2_score}")


if __name__ == "__main__":
    main()
