# list sebagai iterables
warna = ['merah', 'kuning', 'hijau', 'biru', 'abu-abu', 'ungu']
for a in warna:
    print(a)
    print(len(a))
print(len(a))
snakes = "anaconda"
for t in snakes:
    print(t)
Data_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Data_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Data_3 = [warna, Data_1, Data_2]
for SubData3 in Data_3:
    print(SubData3)
    for komponen in SubData3:
        print(komponen)
# for else break dan range
print('=' * 100)
print("for else break dan range")
for i in range(10, 35, 3):
    print(i)
print(range(10, 35, 3))
numbers = 60
for i in range(0, 51):
    print(i)
    if i is numbers:
        print('numbers found', i)
        break
else:
    print('numbers not found')
print('process finished')
