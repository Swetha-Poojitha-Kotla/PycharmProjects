list = [2, 5, 1, 6, 8, 9, 10]
pos = -1
n = 10


def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False


if search(list, n):
    print("Found at ", pos)
else:
    print("not Found")
