#simple infite with conditions

count = 0
while True:
    count += 1
    if count > 100:
        break
    if count % 5 == 0:
        continue
    print(count)
