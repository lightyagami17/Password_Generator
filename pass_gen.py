import string
import random

if __name__ == '__main__':
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    lenp = int(input('Enter The Length of the Password you wish to have... '))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    print('Voila!! The new password as requested is ', end="")
    print("".join(random.sample(s, lenp)))
