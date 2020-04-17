i = 0
while i < 100:
    i += 1
    if i % 7 == 0:
        continue
    if i % 10 == 7:
        continue
    if (i // 10) % 10 == 7:
        continue
    print(i)
