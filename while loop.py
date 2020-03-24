numbers = 0
while numbers < 5:
    print('the numbers is', numbers)
    numbers = numbers + 1
else:
    print('the end of numbers is', numbers)
print('numbers finding is finished')
print('=' * 50)
# variable boolean
start = True
numbers2 = 0
while start:
    print('numbers finding processing')
    numbers2 += 2
    if numbers2 is 20:
        start = False
        print('numbers matched', numbers2)
print('numbers matching finished')
print('=' * 100)
# kombinasi dengan break, continue, and pass
# break
print('=' * 50)
numbers3 = 0
while numbers3 < 20:
    numbers3 = numbers3 + 1
    if numbers3 is 15:
        print('checkpoint 1')
        break
    print('the numbers is', numbers3)
    numbers3 += 1
else:
    print('checkpoint not found')
print('process finished')
# continue
print('=' * 50)
numbers3 = 0
while numbers3 < 20:
    numbers3 = numbers3 + 1
    if numbers3 is 15:
        print('checkpoint 1')
        continue
    print('the numbers is', numbers3)
    numbers3 += 1
else:
    print('checkpoint not found')
print('process finished')
# pass
print('=' * 50)
numbers3 = 0
while numbers3 < 20:
    numbers3 = numbers3 + 1
    if numbers3 is 15:
        print('checkpoint 1')
        pass
    print('the numbers is', numbers3)
    numbers3 += 1
else:
    print('checkpoint not found')
print('process finished')
