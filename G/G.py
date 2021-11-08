n = int(input())

rating = []

for _ in range(n):
    rating.append(int(input()))

bonus = [500 for x in range(n)]

def check_rating_and_bonus(cur):
    left = (cur > 0 and rating[cur - 1] < rating[cur] and bonus[cur - 1] >= bonus[cur])
    right = (cur < n - 1 and rating[cur + 1] < rating[cur] and bonus[cur + 1] >= bonus[cur])
    if left or right:
        return True
    return False

for cur in range(n):
    while check_rating_and_bonus(cur):
        bonus[cur] += 500
        relax = cur - 1
        while (relax >= 0 and check_rating_and_bonus(relax)):
            bonus[relax] += 500
            relax -= 1

# print(bonus)
print(sum(bonus))