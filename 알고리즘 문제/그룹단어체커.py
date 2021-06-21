import re

case = int(input())
count = 0

for _ in range(case):
    string = input()

    for char in string:
        p = re.compile(f'{char}+')
        char_count = len(p.findall(string))
        
        if char_count > 1:
            break
    else:
        count += 1

print(count)
