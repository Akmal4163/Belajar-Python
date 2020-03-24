# fungsi dengan return value
def border():
    print('=' * 100)


def kuadrat(argumen):
    total = argumen ** 2
    print('nilai kuadrat dari argumen adalah:', total)
    return total


print(kuadrat(348))
print('=' * 100)


# fungsi dengan return value dan multiple arguments
def penjumlahan(argumen1, argumen2):
    total = argumen1 + argumen2
    print(argumen1, '+', argumen2, 'hasilnya adalah:', total)
    return total


penjumlahan(34567, 4579)
print(penjumlahan(336, 414))

border()


def perkalian(argumen1, argumen2):
    total = argumen1 * argumen2
    print(argumen1, 'x', argumen2, 'hasilnya adalah:', total)
    return total


a = penjumlahan(324, 333)
b = perkalian(34567, 4579)
print(perkalian(336, a))
c = perkalian(334, penjumlahan(245, 445))
print(c)

# membuat anonymus function dengan lambda
perkalian = lambda x, y: x * y
hasil = perkalian(344, 567)
print(hasil)

# edit variabel menjadi global
name = 'bob'
studying = 'computer science'


def editname(newname):
    global name
    name = newname
    print("the people newname is:", name)


editname('lisa')


def editlearning(newname, newstudy):
    global name, studying
    studying = newstudy
    name = newname
    if name == 'lisa':
        print("the people name is:", name, "and she is learn", studying)
    else:
        print('the people name is:', name, 'and he learn', studying)


editlearning('lisa', 'computer science')
