test_case = int(input())

for _ in range(test_case):
    students = list(map(int, input().split()))
    aver = sum(students[1:]) / students[0]
    result = len(list(filter(lambda x: x > aver, students[1:]))) / students[0] * 100

    print('%.3f%%' % result)
