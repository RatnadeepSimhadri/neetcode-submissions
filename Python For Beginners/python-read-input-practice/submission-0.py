def add_two_numbers() -> int:
    line = input()
    strs = line.split(",") 
    sum=0
    for _str in strs:
        sum += int(_str)
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
