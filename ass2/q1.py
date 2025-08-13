
# starts with lowercase letter and followed by 0 or more lowercase letters

import re

seq = r'[a-z]'

final_seq = r'([a-z])([a-z]*)'

word = input("Enter a string: ")
if re.fullmatch(final_seq, word):
    print("Accepted")
else:
    print("Not Accepted")