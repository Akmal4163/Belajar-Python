data = [1, 2, 3, 4, 5, 6]
# mengakses list
subdata1 = data[3]
subdata2 = data[-3]
subdata3 = data[2:4]
print(subdata3)
data2 = [100, 200, 300, 400, 500, 600]
data[4] = 87
data[3] = 20
# menambah list
data3 = data + data2
print(data3)
a = data + data2 + data3
print(a)
# mengcopy data ke variabel baru
c = data[:]
c[4] = 87
print(data)
# mengubah konten list dengan metode slicing
data[4:5] = [3, 4]
print(data)
data[3] = [7, 8]
print(data)
# list dalam list
x = [data, data2]
print(x)
y = x[0]
print(y)
y = x[0][4]
print(y)
y = x[1][4]
print(y)
# methods untuk list
data.append(30)
print(data)
# function pada data yang bisa kita gunakan pada list
print("panjang listnya berapa?")
panjang_list = len(data+data2)
print(panjang_list)
print(data+data2)
# membuat list kosong
bentuk = []
# kita akan membuat list dengan satu item
hobi = ["membaca"]
# contoh list dengan isi lebih dari satu
warna = ["merah", "kuning", "hijau", "abu-abu", "ungu", ]
# index biasanya berurutan dimulai dari angka 0
# kalau dari sebelah kanan nilainya negatif
print(warna[2])
print(warna[-3])
print(warna[4])
# masukkan nama-nama teman
myfriends = ["gilbeet", "bagus", "aat", "lisan", "adi", "umam", "naufal", ]
# masukkan nama teman dengan nomor indeks 3
print(myfriends[3])
print(myfriends[-3])
# menampilkan semua nama teman
print(myfriends)
# menampilkan jumlah semua data
print("berapa jumlah semua teman?")
print(len(myfriends))
print(hobi)
myfriends = ["gilbeet", "bagus", "aat", "lisan", "adi", "umam", "naufal", ]
print(myfriends)
