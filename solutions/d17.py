import os
import pathlib


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


class Computer():

    def __init__(self, program:list, registers:dict):
        self.pointer = 0
        self.output = []
        self.program = program
        self.a = registers["A"]
        self.b = registers["B"]
        self.c = registers["C"]
        self.stop = False
        self.opcodes = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }
        self.operands = {
            0: lambda: 0,
            1: lambda: 1,
            2: lambda: 2,
            3: lambda: 3,
            4: lambda: self.a,
            5: lambda: self.b,
            6: lambda: self.c,
            7: self.stop_fn
        }
    
    def stop_fn(self):
        self.stop = True

    def adv(self):
        combo = self.operands[self.program[self.pointer+1]]()
        self.a =  int(self.a / (2 ^ combo))
        self.pointer += 2

    def bxl(self):
        self.b = self.b ^ self.program[self.pointer+1]
        self.pointer += 2

    def bst(self):
        combo = self.operands[self.program[self.pointer+1]]()
        self.b = combo % 8
        self.pointer += 2

    def jnz(self):
        if self.a == 0:
            self.pointer += 2
        else:
            combo = self.operands[self.program[self.pointer + 1]]()
            print(f"Resetting pointer from {self.pointer} to {combo}")
            self.pointer = combo

    def bxc(self):
        result = self.b ^ self.c
        self.b = result
        self.pointer += 2

    def out(self):
        combo = self.operands[self.program[self.pointer+1]]()
        out = combo % 8
        self.output.append(out)
        print(f"Outputting {out}")
        self.pointer += 2


    def bdv(self):
        combo = self.operands[self.program[self.pointer+1]]()
        self.b =  int(self.a / (2 ^ combo))
        self.pointer += 2

    def cdv(self):
        combo = self.operands[self.program[self.pointer+1]]()
        self.c =  int(self.a / (2 ^ combo))
        self.pointer += 2

    def process(self):
        print("Starting program")
        while self.stop  == False:
            if self.pointer + 1 >= len(self.program):
                self.stop = True
                break
            print("condition met, proceeding")
            print(f"using func {self.opcodes[self.pointer].__name__} with pointer {self.pointer} on operand {self.program[self.pointer]}")
            self.opcodes[self.program[self.pointer]]()
        print("processing completed")
        return self.output


def p1(data:str) -> int:
    pass


def p2(data:str) -> int:
    pass


def main():

    file = os.path.join(pathlib.Path(__file__).parent.resolve(), "../input", "d17s.txt")

    program, registers = read_input(file)

    computer = Computer(program, registers)

    computer.process()
    print(computer.output)


if __name__ == "__main__":
    main()
