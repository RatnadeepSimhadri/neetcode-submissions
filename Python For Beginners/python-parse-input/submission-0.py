from typing import List

def read_integers() -> List[int]:
    input_str = input()
    input_list = input_str.split(",")
    int_list = []
    for s in input_list:
        int_list.append(int(s))
    return int_list



# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
