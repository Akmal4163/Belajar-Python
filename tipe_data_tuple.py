def borderradius1(sym):
    total = sym * 100
    print(total)


# list
ganjil = [1, 3, 5, 7, 9]
# tuple
genap = (2, 4, 6, 8, 10)
print(type(ganjil))
print(type(genap))
# tuple bersifat tetap dan tidak bisa dirubah nilainya
print(dir(ganjil))
print(dir(genap))
print(genap.count(10))
print(genap.index(10))
# test tuple
import sys

borderradius1('=')
data_list = [1, 2, 3, 4, 5, 'yellow', 'green', 'cars', True, False, 3.14]
data_tuple = (1, 2, 3, 4, 5, 'yellow', 'green', 'cars', True, False, 3.14)

size_datalist = sys.getsizeof(data_list)
size_datatuple = sys.getsizeof(data_tuple)
print('datasize for list:', size_datalist)
print('datasize for tuple:', size_datatuple)
borderradius1('=')
import timeit

data_list1 = timeit.timeit(stmt="[1,2,3,4,5]", number=10000)
data_tuple1 = timeit.timeit(stmt="(1,2,3,4,5)", number=10000)
print('time for processing list:', data_list1)
print('time for processing tuple:', data_tuple1)
borderradius1('=')
# set, himpunan
# tidak berurutan

equipment = {"cpu",
             "monitor",
             "speakers",
             "mouse",
             "printer",
             "keyboard",
             "pen tablet"}
equipment.add("external gpu")
equipment.add("pen tablet")
print(equipment)
# cara lain membuat dataset
borderradius1('=')
cpu = set()
cpu.add("processor")
cpu.add("motherboard")
cpu.add("memory card")
cpu.add(16)
print(cpu)
borderradius1('=')
ganjil = {1, 3, 5, 7, 9}
genap = {2, 4, 6, 8, 10}
prima = {2, 3, 5, 7, }
print(ganjil.union(genap))
print(ganjil.intersection(prima))
borderradius1('=')
# dictionary/kamus
member1 = {"id": 101,
           "nama": "sandhika galih",
           "pekerjaan": "dosen",
           "status member": "platinum"}
member2 = {"id": 102,
           "nama": "faqihza mukhlish",
           "pekerjaan": "asisten dosen",
           "status member": "gold"}
memberlist = {101: member1, 102: member2}
print(memberlist[101])
print(memberlist[102])
borderradius1('=')
print(member1["nama"])
print(member1.keys())
print(member1.values())
print(member1.items())
