queries = int(input())

for query in range(queries):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    l1, l2, r1, r2 = 0, 1, len(a)-1, len(a) - 2

    area = a[l1] * a[r1]
    count = 0
    while l2 < r2:
        if a[l1] != a[l2] or a[r1] != a[r2] or a[l1] * a[r1] != area:
            break
        count += 1
        l1 += 2
        l2 += 2
        r1 -= 2
        r2 -= 2
    if count == n:
        print("YES")
    else:
        print("NO")