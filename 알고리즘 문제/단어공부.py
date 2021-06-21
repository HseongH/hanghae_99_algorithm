string = input().upper()
alpha = [[0, i] for i in range(26)]

for char in string:
    idx = ord(char) - ord('A')
    alpha[idx][0] += 1

max_alpha = max(alpha)
count = 0

for char in alpha:
    if char[0] == max_alpha[0]:
        count += 1

print(chr(alpha[max_alpha[1]][1] + ord('A'))) if count == 1 else print('?')