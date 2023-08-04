from bitstring import Bits

def decimalToBinary_ten(n):
    if(n<0):
        bnr = Bits(int=n,length=10)
        return str(bnr.bin)
    x = bin(n).replace("0b", "")
    x = x[::-1] #this reverses an array
    while len(x) < 10:
        x += '0'
    bnr = x[::-1]
    return bnr

def decimalToBinary_sixteen(n):
    if(n<0):
        bnr = Bits(int=n,length=16)
        return str(bnr.bin)
    x = bin(n).replace("0b", "")
    x = x[::-1] #this reverses an array
    while len(x) < 16:
        x += '0'
    bnr = x[::-1]
    return bnr    


if __name__ == '__main__':
    r_type={   
        'add':'0000',
        'sub':'0001',
        'mul':'0010',
        'div':'0011',
    }

    i_type={
        'addi':'0000',
        'subi':'0001',
        'sw':'0010',
        'lw':'0011',
        'sll':'0100',
        'beq':'0101',
        'bne':'0110'
    }

    j_type={
        'j':'0111',
        'jal':'1000',
        'jr': '1001'
    }

    registers = {
        '$ze' : '000',
        '$t0' : '001',
        '$t1' : '010',
        '$v0' : '011',
        '$ra' : '100',
        '$s0' : '101',
        '$s1' : '110',
        '$s2' : '111',
    }

    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
    file1.seek(0)
    file2 = open('output.txt', 'w')
    for i in range(len(Lines)):
        binary_code = []
        operation = Lines[i].split(" ")[0]
        print(operation)
        if operation in r_type:
            func = r_type[operation]
            opcode = '0000'
            shamt = '000'
            rs = Lines[i].split(" ")[1][0:3]
            rs_bin = registers[rs]
            rt = Lines[i].split(" ")[2][0:3]
            rt_bin = registers[rt]
            rd = Lines[i].split(" ")[3][0:3]
            rd_bin = registers[rd]
            binary_code.extend([opcode,rs_bin,rt_bin,rd_bin,shamt,func])
            for element in binary_code:
                file2.write(element + "")
            file2.write("\n")
            
        elif operation in i_type:
            opcode = i_type[operation]
            rs = Lines[i].split(" ")[1][0:3]
            rs_bin = registers[rs]
            rt = Lines[i].split(" ")[2][0:3]
            rt_bin = registers[rt]
            immediate = Lines[i].split(" ")[3]
            immediate = int(immediate)
            immediate_bin = decimalToBinary_ten(immediate)
            binary_code.extend([opcode,rs_bin,rt_bin,immediate_bin])
            for element in binary_code:
                file2.write(element + "")
            file2.write("\n")
        
        elif operation in j_type:
            if operation == 'jal':
                label = Lines[i].split(" ")[1]
                label = label.rstrip() + ':'
                for number, line in enumerate(file1):
                     if (label) in line:
                        line_number = number
                        print(line_number)
                        print('hello')
                        break
                opcode = j_type[operation]
                target_address_bin = decimalToBinary_sixteen(line_number)
                binary_code.extend([opcode,target_address_bin])
                for element in binary_code:
                    file2.write(element + "")
                file2.write("\n")
                ra = i
                print(ra)
            elif operation == 'jr':
                opcode = j_type[operation]
                target_address_bin = decimalToBinary_sixteen(ra)
                binary_code.extend([opcode,target_address_bin])
                for element in binary_code:
                    file2.write(element + "")
                file2.write("\n")
                
            else:
                opcode = j_type[operation]
                target_address = int(Lines[i].split(" ")[1])
                target_address_bin = decimalToBinary_sixteen(target_address)
                binary_code.extend([opcode,target_address_bin])
                for element in binary_code:
                    file2.write(element + "")
                file2.write("\n")





