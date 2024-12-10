import os
import pathlib
import copy
from collections import deque


def read_input(file: str) -> list:
    with open(file) as f:
        lines = f.readlines()
        data = "".join(lines)
    return data.strip()


def format_sys(data:str) -> tuple[deque, dict]:
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


def checksum(file_sys:dict) -> int:
    score = 0
    for obj_id, positions in file_sys.items():
        for pos in positions:
            score += obj_id * pos
    return score


def compress(file_sys:dict, empty:list) -> dict:
    for obj in reversed(file_sys):
        if len(empty) > 0:
            for pos in range(len(file_sys[obj])):
                if len(empty) > 0 and empty[0] < file_sys[obj][-1]:
                    file_sys[obj].pop()
                    file_sys[obj].appendleft(empty.popleft())
        else:
            break
    print(file_sys)
    print(empty)
    return file_sys


def check_empty_block(empty: list, min_length: int, pos: int) -> tuple:
    # Exit if reach empty list size
    if pos >= len(empty):
        return None, pos
    length = 1 # starting length
    orig_pos = pos
    # Determine size for current empty block
    for i in range(len(list(empty)[pos:]) - 1):
        if empty[pos] == empty[pos+1] - 1 and empty[pos]:
            length += 1
            pos += 1
        else:
            break
    # Return if empty block meets conditions
    if length >= min_length:
        return length, orig_pos
    # If not, check next empty block
    else:
        pos += 1
        return check_empty_block(empty, min_length, pos)


def compress_whole(file_sys:dict, empty:list) -> dict:
    empty = list(empty)
    for obj, idxs in reversed(file_sys.items()):
        if len(idxs) == 0:
            pass
        elif len(empty) > 0 and idxs[0] > empty[0]:
            empty_found, pos = check_empty_block(empty, len(idxs), 0)
            if empty_found and pos < idxs[0]:
                pass
                for i in range(len(idxs)):
                    idxs.pop()
                    idxs.appendleft(empty[pos])
                    del empty[pos]
            print(f"Moved obj {obj}")
    return file_sys


def p2(data:str) -> int:
    pass


def main():

    file = os.path.join(pathlib.Path(__file__).parent.resolve(), "../input", "d09s.txt")
    data = read_input(file)

    file_sys, empty = format_sys(data)

    p1_file_sys = copy.deepcopy(file_sys)
    compressed = compress(p1_file_sys, empty.copy())
    p1_score = checksum(compressed)
    print(f"Part 1 score: {p1_score}")

    # p2_file_sys = copy.deepcopy(file_sys)
    # compressed_whole = compress_whole(p2_file_sys, empty.copy())
    # p2_score = checksum(compressed_whole)
    # print(f"Part 2 score: {p2_score}")


if __name__ == "__main__":
    main()
