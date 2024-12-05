import os
import pathlib


def read_input(file: str) -> list:
    left = []
    right = []
    with open(file) as f:
        for line in f.readlines():
            nums = line.split()
            left.append(int(nums[0]))
            right.append(int(nums[1]))
    return left, right


def p1(left: list, right: list) -> int:
    score = 0
    for x in range(len(left)):
        diff = abs(left[x] - right[x])
        score += diff
    return score


def p2(left: list, right: list) -> int:
    score = 0
    for x in left:
        count = 0
        for y in right:
            if x == y:
                count += 1
        score += x * count
    return score


def main():

    file = os.path.join(pathlib.Path(__file__).parent.resolve(), "../input", "d01.txt")

    left, right = read_input(file)
    l_sorted = sorted(left)
    r_sorted = sorted(right)

    p1_score = p1(l_sorted, r_sorted)
    print(f"Part 1 score: {p1_score}")

    p2_score = p2(l_sorted, r_sorted)
    print(f"Part 2 score: {p2_score}")


if __name__ == "__main__":
    main()
