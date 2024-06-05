def int_to_roman(num):
    numb = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80,
            70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    alph = ["M", "CM", "DCCC", "DCC", "DC", "D", "CD", "CCC", "CC", "C", "XC", "LXXX", "LXX", "LX",
            "L", "XL", "XXX", "XX", "X", "IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I"]

    roman_num = ''

    for i in range(len(numb)):
        while num >= numb[i]:
            roman_num += alph[i]
            num -= numb[i]
    return roman_num


def roman_to_int(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for char in reversed(roman):
        value = roman_dict[char]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result


#print(int_to_roman(1000))
#print(roman_to_int("M"))
