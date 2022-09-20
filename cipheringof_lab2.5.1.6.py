# #asks the user for one line of text to encrypt;
# asks the user for a shift value (an integer number from the range 1..25 -
# note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
# prints out the encoded text.
# Test your code using the data we've provided.

text = input("enter any text. ")
shift = int(input("enter the shift value in between 1 to 25."))
code = ""
current_char = ""
for ch in text:
    if not ch.isalpha():
        current_char = ch

    else:
        if ch.islower():
            num = ord(ch)
            num += shift
            if num <= ord('z'):
                current_char = chr(num)
            else:
                new_shift = num - ord('z')
                new_ch = new_shift + ord('a') - 1
                current_char = chr(new_ch)
        else:
            num = ord(ch)
            num += shift
            if num <= ord('Z'):
                current_char = chr(num)
            else:
                new_shift = num - ord('Z')
                new_ch = new_shift + ord('Z') - 1
                current_char = chr(new_ch)
    code += current_char



print(code)
