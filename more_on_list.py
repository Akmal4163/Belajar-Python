def borderradius1(sym):
    total = sym*100
    print(total)
borderradius1('=')
utility = ['locks', 'chambers', 'cars', 'jackets', 'wheels']
print(utility)
# list manipulation
# method untuk menambah list
borderradius1('=')
utility.append('equipment')
print(utility)
data = 'test'
for i in data:
    print(data[2])
# menambahkan data
borderradius1('=')
utility.extend('cables')
print(utility)
utility.insert(2, 'cycles')
print(utility)
# method untuk menambah anggota
borderradius1('=')
utilitylength = utility.count('cycles')
print('the count of utility is:', utilitylength)
# meremove data
borderradius1('=')
utility.remove('cycles')
print(utility)
utility.reverse()
print(utility)
stuff = utility.copy()
stuff.append('glass')
print(stuff)
print(utility)
