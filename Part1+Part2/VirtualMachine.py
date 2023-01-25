# Please enter the name of the file you wish to read
import sys

file_name = "input-1.asm"

# Create a dictionary to hold the register values
registers = {}

# Define the functions to execute each instruction

# Add the values of the registers x and y and store the result into the x register
def add(x, y):
    registers[x] += registers[y]


# Copy the value of y (which could be a constant or the contents of a register) into register x
def mov(x, y):
    if y.isalpha():
        registers[x] = registers[y]
    else:
        registers[x] = int(y)


# Print the Unicode representation of the value in the register x to stdout (without a newline character).
def print_reg(x):
    print(chr(registers[x]), end='')


# Jump to the instruction `y` steps away (forward for positive values of y,
# backward for negative values of y),
# but only if `x` (a constant or register) is non-zero (Jump Not Zero).
def jnz(x, y):
    if x.isalpha():
        x = registers[x]
    else:
        x = int(x)
    if x != 0:
        if y.isalpha():
            return registers[y]
        else:
            return int(y)
    else:
        return None


# initialize the values of the registers x and y
def initialize_register(x, y):
    if x not in registers:
        registers[x] = 0
    if y not in registers:
        registers[y] = 0


# open the file
try:
    with open(file_name) as f:
        instructions = f.readlines()
except IOError:
    print("Cannot read the file")
    sys.exit()


# Start the Program After reading
i = 0
while i < len(instructions):
    instruction = instructions[i].strip().split()
    getTheNameOfFun = instruction[0]

    # Check the operation and call the corresponding function
    if getTheNameOfFun == "add":
        x, y = instruction[1], instruction[2]
        initialize_register(x, y)
        add(x, y)

    elif getTheNameOfFun == "mov":
        x, y = instruction[1], instruction[2]
        if x not in registers:
            registers[x] = 0
        mov(x, y)

    elif getTheNameOfFun == "print":
        x = instruction[1]
        if x not in registers:
            registers[x] = 0
        print_reg(x)

    elif getTheNameOfFun == "jnz":
        x, y = instruction[1], instruction[2]
        initialize_register(x, y)
        jmp = jnz(x, y)
        if jmp is not None:
            i += jmp
            continue

    i += 1
