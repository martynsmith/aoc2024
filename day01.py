from pathlib import Path

data = Path('sample01.txt').read_text().splitlines()
data = Path('input01.txt').read_text().splitlines()

l1, l2 = zip(*(map(int, row.split()) for row in data))

print('Part 1:', sum(abs(b-a) for a, b in zip(sorted(l1), sorted(l2))))
print('Part 2:', sum(n * l2.count(n) for n in l1))

