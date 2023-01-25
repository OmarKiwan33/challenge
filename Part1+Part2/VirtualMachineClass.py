import sys

class VirtualMachine:
    def __init__(self, file_name):
        self.registers = {}
        self.instructions = []
        self.instruction_ptr = 0
        self.file_name = file_name

        # open the file
        try:
            with open(self.file_name) as f:
                self.instructions = f.readlines()
        except IOError:
            print("Cannot find the file")
            sys.exit()

    # Add the values of the registers x and y and store the result into the x register
    def add(self, x, y):
        self.registers[x] += self.registers[y]

    # Copy the value of y (which could be a constant or the contents of a register) into register x
    def mov(self, x, y):
        if y.isalpha():
            self.registers[x] = self.registers[y]
        else:
            self.registers[x] = int(y)

    # Print the Unicode representation of the value in the register x to stdout (without a newline character).
    def print_register(self, x):
        print(chr(self.registers[x]), end='')

    # Jump to the instruction `y` steps away (forward for positive values of y,
    # backward for negative values of y),
    # but only if `x` (a constant or register) is non-zero (Jump Not Zero).
    def jnz(self, x, y):
        if x.isalpha():
            x = self.registers[x]
        else:
            x = int(x)
        if x != 0:
            if y.isalpha():
                return self.registers[y]
            else:
                return int(y)
        else:
            return None

    # initialize the values of the registers x and y
    def initialize_register(self,x, y):
        if x not in self.registers:
            self.registers[x] = 0
        if y not in self.registers:
            self.registers[y] = 0

    def run(self):
        # Start the Program
        while self.instruction_ptr < len(self.instructions):
            instruction = self.instructions[self.instruction_ptr].strip().split()
            getTheNameOfFun = instruction[0]

            # Check the operation and call the corresponding function
            if getTheNameOfFun == "add":
                x, y = instruction[1], instruction[2]
                self.initialize_register(x, y)
                self.add(x, y)

            elif getTheNameOfFun == "mov":
                x, y = instruction[1], instruction[2]
                self.initialize_register(x, y)
                self.mov(x, y)

            elif getTheNameOfFun == "print":
                x = instruction[1]
                self.initialize_register(x, None)
                self.print_register(x)

            elif getTheNameOfFun == "jnz":
                x, y = instruction[1], instruction[2]
                self.initialize_register(x, y)
                jmp = self.jnz(x, y)
                if jmp is not None:
                    self.instruction_ptr += jmp
                    continue

            self.instruction_ptr += 1


def main():
    #pleas write the File name
    vm = VirtualMachine("input-3.asm")
    vm.run()


if __name__ == "__main__":
    main()
