EMPTY = 0
OPEN = 2
MINE = 1

def add_candidates(candidates, field, x, y, n, m):
    if x > 0 and field[x - 1][y] == EMPTY:
        candidates.add((x - 1, y))
    if x < n - 1 and field[x + 1][y] == EMPTY:
        candidates.add((x + 1, y))
    if y > 0 and field[x][y - 1] == EMPTY:
        candidates.add((x, y - 1))
    if y < m - 1 and field[x][y + 1] == EMPTY:
        candidates.add((x, y + 1))

def open_field(field, x, y, n, m):
    # print(f"open_field({x}, {y}")
    marked = set()
    marked.add((x, y))
    field[x][y] = OPEN
    candidates = set()
    add_candidates(candidates, field, x, y, n, m)
    while candidates:
        x, y = candidates.pop()
        field[x][y] = OPEN
        add_candidates(candidates, field, x, y, n, m)

n, m = (int(x) for x in input().split())
k = int(input())

field = [[EMPTY for x in range(m)] for y in range(n)]
# print(field)
for _ in range(k):
    r, c = (int(x) for x in input().split())
    field[r-1][c-1] = MINE

# print(field)
counter = 0
for r in range(n):
    for c in range(m):
        if field[r][c] != EMPTY:
            continue
        open_field(field, r, c, n, m)
        counter += 1

print(counter)