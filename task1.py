bits = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
for i,bit in enumerate(bits):
    try:
        bit = int(input(f"Please enter bit {i} mode: "))
        if bit in range(0 , 2):
            bits[i] = str(bit)
        else:
            bit = int(input(f"Undefined mode.Please enter bit {i} mode again: "))
    except ValueError:
        bit = int(input(f"Invalid input. Please enter the bit {i} mode in number 0 for Input, 1 for Output: "))
        if bit in range(0 , 2):
            bits[i] = str(bit)
        else:
            bit = int(input(f"Undefined mode.Please enter bit {i} mode again: "))
num ="".join(bits)
file = open("file.c" , "a")
file.write("void Init_voidPortADir (void)\n")
file.write("{")
file.write("\n\tDDRA = 0b"+num+";\n")
file.write("}")