from queue import PriorityQueue

n, x, k = (int(v) for v in input().split())
dead = [int(x) for x in input().split()]

q = PriorityQueue()
for d in dead:
    q.put(d)

# print(n, x, k)
# print(dead)

day = 0
while k > 0:
    new_day = q.get()
    q.put(new_day + x)
    if new_day != day:
        k -= 1
    day = new_day
    # print(day, k)

print(day)
