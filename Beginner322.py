n, m = map(int, input().split())
s = input()
t = input()
if t.startswith(s):
    if t.endswith(s):
        print(0)
    else:
        print(1)
elif t.endswith(s):
    if not t.startswith(s):
        print(2)
else:
    print(3)
