import os
import pathlib
import copy
from collections import deque


def read_input(file: str) -> tuple[list, dict]:
    with open(file) as f:
        registers = {}
        for l in f.readlines():
            if l.startswith("Register A"):
                registers["A"] = int(l.split(" ")[-1])
            elif l.startswith("Register B"):
                registers["B"] = int(l.split(" ")[-1])
            elif l.startswith("Register C"):
                registers["C"] = int(l.split(" ")[-1])
            elif l.startswith("Program: "):
                program = [int(x) for x in l.split(" ")[-1].split(",")]
    return program, registers


class register():

    def __init__(program:list, registers:dict):
        self.pointer = 0
        self.output = []
        self.program = program
        for k,v in registers.items():
            self.k = v
        self.opcodes = {
            0: self.adv(),
            1: self.bxl(),
            2: self.bst(),
            3: self.jnz(),
            4: self.bxc(),
            5: self.out(),
            6: self.bdv(),
            7: self.cdv(),
        },
        self.operands = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: self.a,
            5: self.b,
            6: self.c,
            7: self.stop(),
        },
        self.stop():
            return self.output
    



    def adv(operand):
        out = self.a / (2 ^ operand)
        out = round(out)
        self.a = out

    def bxl(operand):
        return self.b ^ self.operands(operand)

    def bst(operand):
        out = operand % 8
        self.b = out
    

    def jnz(operand):
        if self.a == 0:
            pass
        else:
            self.pointer = self.operand

    def bxc():
        out = self.b ^ self.c
        self.b = out

    def out():
        out = operand % 8
        self.output.append(out)

    def bdv():
        out = self.a / (2 ^ operand)
        out = round(out)
        self.b = out

    def cdv():
        out = self.a / (2 ^ operand)
        out = round(out)
        self.c = out

    


class program():

    def __init__():


def p1(data:str) -> int:
    pass


def p2(data:str) -> int:
    pass


def main():

    file = os.path.join(pathlib.Path(__file__).parent.resolve(), "../input", "d17s.txt")
    program, registers = read_input(file)
    print(program)
    print(registers)
if __name__ == "__main__":
    main()
