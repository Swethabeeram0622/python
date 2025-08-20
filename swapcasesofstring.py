#Task is to swap cases of given string, convert all lowercase letters to uppercase letters and vice versa.
def swap_case(s):
    txt = ""
    for char in s:
        if char.isupper():
            txt += char.lower()
        else:
            txt += char.upper()
    return txt 
