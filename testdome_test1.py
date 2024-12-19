import string

def numbers_to_letters(s):
    conv_table = {}
    phrase = ''
    for i in range(26):
        conv_table[i+1]= chr(ord('A')+i)
    space_ind = 0
    for i, x in enumerate(s):
        if x==' ':
            number = s[space_ind:i]
            phrase += str(conv_table[int(number)])
            space_ind = i
        if x=='+':
            number = s[space_ind:i]
            phrase += str(conv_table[int(number)])+' '
            space_ind = i

    number = s[space_ind:len(s)]
    phrase += str(conv_table[int(number)])
    return phrase
 
if __name__ == "__main__":
    print(numbers_to_letters('20 5 19 20+4 15 13 5'))