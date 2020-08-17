## Platforms required using def
def ptRequired(n, arrival, dept):
  arrival.sort()
  dept.sort()
  platforms = 1
  ans = 1
  left = 1
  right = 0
  while left < n and right < n:
    if arrival[left] <= dept[right]: 
      ## if train 2 comes before train 1 departures, then we need extra pt.
      platforms += 1
      left += 1
    elif arrival[left] > dept[right]:
      ## In this case we don't need extra platform
      platforms -= 1
      right += 1
    if platforms > ans:
      ans = platforms
  return ans

n = int(input())
arrival = []
dept = []
for _ in range(n):
  a, d = [int(x) for x in input().split()]
  arrival.append(a)
  dept.append(a+d)

print(ptRequired(n, arrival, dept))
