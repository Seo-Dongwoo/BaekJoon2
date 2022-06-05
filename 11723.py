import sys
N = int(sys.stdin.readline())
S = set()

for _ in range(N):
    temp = sys.stdin.readline().strip().split()

    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1,21)])
        else:
            S = set()
        continue

    command, target = temp[0], temp[1]
    target = int(target)

    if command == "add":
        S.add(target)
    elif command == "check":
        print(1 if target in S else 0)
    elif command == "remove":
        S.discard(target)
    elif command == "toggle":
        if target in S:
            S.discard(target)
        else:
            S.add(target)

