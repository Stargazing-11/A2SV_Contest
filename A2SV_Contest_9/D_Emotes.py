n, m , k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

val = (arr[0] * k + arr[1]) * (m // (k+1)) + (arr[0] * (m % (k+1)))
print(val)