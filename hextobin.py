
Hex_File = open("COTS.hex" , "r")
bin_File = open("COTS.bin" , "a")

for line in Hex_File:
    binary = ""
    for char in line:
        if char==":":
            continue
        elif char=="\n":
            bin_File.write(binary + "\n")
            break
        binary += str(bin(int(char, 16))[2:].zfill(4))
        
    