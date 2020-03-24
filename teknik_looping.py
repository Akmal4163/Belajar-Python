import tipe_data_tuple
tipe_data_tuple.borderradius1('=')


# teknik looping

nama_channel = ['kelas terbuka',
                'web programming unpas',
                'sekolah koding',
                'kawan koding',
                'universitas koding',
                'dicoding']
konten = ['belajar python',
          'belajar javascript',
          'belajar php',
          'belajar java',
          'belajar kotlin',
          'belajar c++']
# enumerate
for index, channel in enumerate(nama_channel):
    print(index, ':', channel)

for channel, konten2 in zip(nama_channel, konten):
    print(channel, ':', 'materi kelas ini adalah:', konten2)

# melooping set
playlist = {'belajar reactJS', 'belajar vueJS', 'belajar bootstrap', 'belajar laravel', 'belajar codeigniter',
            'belajar android'}
for materi in sorted(playlist):
    print(materi)
# melooping dictionary
playlist2 = {'kelas terbuka': 'belajar python',
             'web programming unpas': 'belajar javascript',
             'sekolah koding': 'belajar php',
             'kawan koding': 'belajar java',
             'universitas koding': 'belajar kotlin',
             'dicoding': 'belajar c++'}
for i, v in playlist2.items():
    print(i, 'materinya', v)

for i in reversed(range(1,10,1)):
    print(i)

tipe_data_tuple.borderradius1('=')
