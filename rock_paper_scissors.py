#Steve
#10.25

import random
def who_wins(u, c):
    # 1 is rock, 2 is paper, 3 is scissors
    while True:
        if u == 3 and c == 1 or u == 1 and c==3:
            return min(u, c)
        elif u == c:
            return 0
        else:
            return max(u, c)

    pass
dic = {1: 'rock', 2: 'paper', 3: 'scissor' }

def main():
    a = int(input())
    b = random.randint(1,3)
    who_wins(a, b)
    if who_wins(a, b) == a:
        print(f'user win (user:{dic[a]} vs computer:{dic[b]})')
    elif who_wins(a, b) == 0:
        print('it\'s a tie')
    else:
        print(f'computer win (user: {dic[a]} vs computer: {dic[b]})')
    pass


if __name__ == '__main__':
    main()