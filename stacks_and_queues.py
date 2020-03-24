def borderradius1(sym):
    total = sym * 100
    print(total)


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('present data:', data)
# memasukkan data baru
borderradius1('=')
data.append(11)
print('input data', 11)
data.append(12)
print('input data', 12)
if data == 'input data':
    print('input data', data)
print('present data', data)
output = data.pop()
print('output data', output)
print('present data', data)
# queues atau antrian
borderradius1('=')
from collections import deque

antrian = deque([1, 2, 3, 4, 5])
print('present data:', antrian)
# menambah data
antrian.append(6)
print('insert data:', 6)
print('present data', antrian)

antrian.append(7)
print('insert data:', 7)
print('present data', antrian)
# mengurangi antrian
output = antrian.popleft()
print('data output', output)
print('present data:', antrian)

output = antrian.popleft()
print('data output', output)
print('present data:', antrian)

output = antrian.popleft()
print('data output', output)
print('present data:', antrian)
