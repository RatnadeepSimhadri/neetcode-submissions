from typing import List

def read_integers() -> List[int]:
    input_list = input()
    string_list = input_list.split(",")
    ans_list = []
    for num_string in string_list:
        ans_list.append(int(num_string))
    return ans_list
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
