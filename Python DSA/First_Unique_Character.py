
from collections import Counter

def First_Unique_Character(s):
    for i,ch in enumerate(s):
        if s.count(ch) == 1:
            return i

s = "loveleetcode"
if __name__ == "__main__":
    print(First_Unique_Character(s))
    