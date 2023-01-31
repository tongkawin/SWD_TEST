num = 1111 # input number here
string = str(num)
roman = ""
for i in range(len(string))[::-1]:
    if i==len(string)-1:
        if string[i] == "1": roman = "I"
        elif string[i] == "2": roman = "II"
        elif string[i] == "3": roman = "III"
        elif string[i] == "4": roman = "IV"
        elif string[i] == "5": roman = "V"
        elif string[i] == "6": roman = "VI"
        elif string[i] == "7": roman = "VII"
        elif string[i] == "8": roman = "VIII"
        elif string[i] == "9": roman = "IX"
    elif i == len(string) - 2:
        if string[i] == "1": roman = "X" + roman
        elif string[i] == "2": roman = "XX" + roman
        elif string[i] == "3": roman = "XXX" + roman
        elif string[i] == "4": roman = "XL" + roman
        elif string[i] == "5": roman = "L" + roman
        elif string[i] == "6": roman = "LX" + roman
        elif string[i] == "7": roman = "LXX" + roman
        elif string[i] == "8": roman = "LXXX" + roman
        elif string[i] == "9": roman = "XC" + roman
    elif i == len(string) - 3:
        if string[i] == "1": roman = "C" + roman
        elif string[i] == "2": roman = "CC" + roman
        elif string[i] == "3": roman = "CCC" + roman
        elif string[i] == "4": roman = "CD" + roman
        elif string[i] == "5": roman = "D" + roman
        elif string[i] == "6": roman = "DC" + roman
        elif string[i] == "7": roman = "DCC" + roman
        elif string[i] == "8": roman = "DCCC" + roman
        elif string[i] == "9": roman = "CM" + roman
    elif i == len(string) - 4:
        if string[i] == "1": roman = "M" + roman
        elif string[i] == "2": roman = "MM" + roman
        elif string[i] == "3": roman = "MMM" + roman

print(roman)
