import string
import random
import sys

def random_strings(size=8, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

with open(sys.argv[1], "a+") as data:
        created = 0
        while created != 50000:
            string = random_strings()
            data.write(string + "\n")
            created += 1
            sys.stdout.write("\rCreating password: {} out of 50000".format(created))
            sys.stdout.flush()

