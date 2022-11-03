# Password Generator by Daniel Villarroel Chanlopkova
# passgen v.1.0

#password = "" # chars > 8 and chars <= 16
              # at least one capital letter (ASDDFG)
              # At least one number (0 - 9)
              # at least one lower letter

import random, re

pass_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
pass_chars_len=len(pass_chars)
pass_len = random.randint(9, 16)

def password_generator():
    password=""
    for i in range(pass_len):
        password += pass_chars[random.randint(0, pass_chars_len-1)]

    if not re.search(r'[0-9][A-Z][a-z]', password):
        password_generator()



    return password




print(password_generator())