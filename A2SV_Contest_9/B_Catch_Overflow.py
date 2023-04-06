lines = int(input())
stk = []
overflow = 2 ** 32

for _ in range(lines):
    opr = input()

    if opr == 'end':
        curr = 0
        while stk and stk[-1][0] != 'f':
            curr += int(stk.pop())

        _, val = stk.pop().split()
        new = curr * int(val)
        
        if new >= overflow:
            print('OVERFLOW!!!')
            exit()

        stk.append(str(new))
    elif opr == 'add':
        stk.append('1')
    else:
        stk.append(opr)

res = sum(map(int, stk))
print(res if res < overflow else 'OVERFLOW!!!')