from sys import stdin

n = int(stdin.readline())
color_paper = [stdin.readline().split() for _ in range(n)]

blue_paper = 0
white_paper = 0

def cut(paper):
    global blue_paper, white_paper

    if len(paper) <= 1:
        if paper[0][0] == '1':
            blue_paper += 1
        elif paper[0][0] == '0':
            white_paper += 1
        return

    is_blue, is_white = False, False

    for part in paper:
        if '1' in part: is_blue = True
        if '0' in part: is_white = True

        if is_blue and is_white:
            break
    else:
        if is_blue:
            blue_paper += 1
        elif is_white:
            white_paper += 1
        return
    
    half = len(paper) // 2
    top = paper[:half]
    bottom = paper[half:]

    top_left = [top[i][:half] for i in range(half)]
    top_right = [top[i][half:] for i in range(half)]
    bottom_left = [bottom[i][:half] for i in range(half)]
    bottom_right = [bottom[i][half:] for i in range(half)]

    cut(top_left)
    cut(top_right)
    cut(bottom_left)
    cut(bottom_right)

cut(color_paper)

print(white_paper)
print(blue_paper)
