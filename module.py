print('ini adalah modul')
data = 'ini adalah modul data'

def check_module():
    print('module checked')

import mtk

mtk.tambah(2,3)

import mtk as math
math.kurang(34,45)
from mtk import tambah, kurang
tambah(2,44)
kurang(2,33)
from mtk import tambah as t
t(2,3)