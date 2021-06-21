from sys import stdin

calculation = [list(map(int, cal.split('+'))) for cal in stdin.readline().split('-')]
result = sum(calculation[0])

for i in range(1, len(calculation)):
    result -= sum(calculation[i])

print(result)
