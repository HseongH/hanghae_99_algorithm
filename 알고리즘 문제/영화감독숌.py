from sys import stdin

n = int(stdin.readline())
movie_name = 666
count = 0

while True:
    if '666' in str(movie_name):
        count += 1
    if count == n:
        print(movie_name)
        break
    movie_name += 1
