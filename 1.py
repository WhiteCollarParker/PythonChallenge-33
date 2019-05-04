def decodeF(input):
    output = ""
    for char in input:
        if char == ' ':
            output += ' '
            continue
        elif ord(char) == 121:
            output += chr(97)
        elif ord(char) == 122:
            output += chr(98)
        elif ord(char) in range(65,123):
            output += chr(ord(char) + 2)
            continue
        else:
            output += char
            continue
    
    return output
print(ord('a'))

input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


print(decodeF(intput))


# I had to look at the forums to understand that all I had translate was MAP

print(decodeF("map"))


# Just looked up the proposed solution. Makes me laugh)))))