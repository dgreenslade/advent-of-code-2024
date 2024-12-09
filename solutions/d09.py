import os
import pathlib
from collections import deque


def read_input(file: str) -> list:
    with open(file) as f:
        lines = f.readlines()
        data = "".join(lines)
    return data.strip()


def format_sys(data:str) -> list:
    """
    Returns two objects: empty and file_sys
    empty_idx = [idx1,idx2,...]
    file_sys = {
        obj_id: [idx1,idx2,...],
    }
    """
    file_sys = {}
    empty = deque([])
    obj_id = 0
    pos = 0
    for i, char in enumerate(data):
        num = int(char)
        pos_range = [x for x in range(pos, pos + num)]
        if i % 2 == 0:
            file_sys[obj_id] = deque(pos_range)
            obj_id += 1
        else:
            empty += pos_range
        pos += num
    return file_sys, empty


def score(file_sys:dict) -> int:
    score = 0
    for obj_id, positions in file_sys.items():
        for pos in positions:
            score += obj_id * pos
    return score


def compress(file_sys:dict, empty:list) -> int:
    for obj in reversed(file_sys):
        if len(empty) > 0:
            for pos in range(len(file_sys[obj])):
                if len(empty) > 0 and empty[0] < file_sys[obj][-1]:
                    file_sys[obj].pop()
                    file_sys[obj].appendleft(empty.popleft())
        else:
            break
    return file_sys


def p2(data:str) -> int:
    pass


def main():

    file = os.path.join(pathlib.Path(__file__).parent.resolve(), "../input", "d09.txt")
    data = read_input(file)

    file_sys, empty = format_sys(data)

    compressed = compress(file_sys, empty)
    p1_score = score(compressed)
    print(f"Part 1 score: {p1_score}")

    
    # p2_score = p2(data)
    # print(f"Part 2 score: {p2_score}")


if __name__ == "__main__":
    main()
