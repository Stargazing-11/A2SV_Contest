n, d = map(int, input().split())
players = list(map(int, input().split()))

players.sort(reverse=True)

right = len(players) - 1
teams = 0

for left in range(len(players)):
    maxVal = players[left]
    count = 1
    while left < right and (maxVal * count) <= d:
        count += 1
        maxVal = max(maxVal, players[right])
        right -= 1
    if maxVal * count > d:
        teams += 1
print(teams)