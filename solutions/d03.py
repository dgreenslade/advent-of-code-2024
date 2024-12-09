import os
import pathlib
import re


def read_input(file: str) -> list:
    with open(file) as f:
        lines = f.readlines()
        data = "".join(lines)
    return data


def calculate_mul(mul_str:str) -> list:
    nums = re.sub(r"[mul\(\)]", "", mul_str).split(",")
    return int(nums[0]) * int(nums[1])


def p1(data:str) -> int:
    score = 0
    matches = re.findall(r"mul\(\d+\,\d+\)", data)
    for match in matches:
        score += calculate_mul(match)
    return score


def p2(data:str) -> int:
    score = 0
    # remove linebreaks as causing issues
    data = re.sub(r"\n+", "", data)
    dont_removed = re.sub(r"don\'t\(\)(.*?)(?=do\(\)|$)", "", data)
    mul_matchets = re.findall(r"mul\(\d+\,\d+\)", dont_removed)
    for match in mul_matchets:
        score += calculate_mul(match)
    return score


def main():

    file = os.path.join(pathlib.Path(__file__).parent.resolve(), "../input", "d03.txt")
    data = read_input(file)

    p1_score = p1(data)
    print(f"Part 1 score: {p1_score}")
    
    p2_score = p2(data)
    print(f"Part 2 score: {p2_score}")


if __name__ == "__main__":
    main()
