import random
import string
def random_pass():
    pass_len = 6
    charValue = string.ascii_letters + string.digits
    password = "".join([random.choice(charValue) for i in range(pass_len)])
    print(password)
    return password
random_pass()