numbers = 30
for i in range(0, 11):
    print(i)
for z in range(1, 40, 5):
    print(z)
    if z is numbers:
        print('numbers found', z)
        break
else:
    print('numbers not found')
print('number collecting is finished')
# continue and pass
print('=' * 100)
numbers2 = 25
for c in range(0, 50, 5):
    print('numbers found', c)
    if c is numbers2:
        print('you found match numbers', numbers2)
        pass
else:
    print('numbers not found')
print('numbers finding is finished')
