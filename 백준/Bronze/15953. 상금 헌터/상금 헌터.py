def festival2017(rank):
    if rank == 0:
        return 0
    elif rank == 1:
        return 5000000
    elif rank <= 3:
        return 3000000
    elif rank <= 6:
        return 2000000
    elif rank <= 10:
        return 500000
    elif rank <= 15:
        return 300000
    elif rank <= 21:
        return 100000
    else:
        return 0


def festival2018(rank):
    if rank == 0:
        return 0
    elif rank == 1:
        return 5120000
    elif rank <= 3:
        return 2560000
    elif rank <= 7:
        return 1280000
    elif rank <= 15:
        return 640000
    elif rank <= 31:
        return 320000
    else:
        return 0


t = int(input())

for _ in range(t):
    i, j = map(int, input().split())
    print(festival2017(i) + festival2018(j))
