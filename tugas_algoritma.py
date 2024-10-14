biodata_list = [
    {'nama': 'asep', 'umur': 20, 'tinggi badan': 180, 'berat badan': 65, 'riwayat penyakit': 'tidak ada'},
    {'nama': 'yanto', 'umur': 30, 'tinggi badan': 165, 'berat badan': 80, 'riwayat penyakit': 'ada'},
    {'nama': 'chulo', 'umur': 19, 'tinggi badan': 178, 'berat badan': 66, 'riwayat penyakit': 'tidak ada'}
]
nama = str(input('Masukan nama: '))
umur = int(input('Masukan umur: '))
tinggi = int(input('Masukan tinggi badan: '))
berat = int(input('Masukan berat badan: '))
penyakit = str(input('Masukan riwayat penyakit: '))

persyaratan_tinggi_min = 175
persyaratan_berat_max = 70
riwayat_penyakit_tidak_ada = 'tidak ada'

if (umur <= 20) and (tinggi >= persyaratan_tinggi_min) and (penyakit == riwayat_penyakit_tidak_ada) and (berat <= persyaratan_berat_max):
    hasil = 'Lolos seleksi'
else:
    hasil = 'Tidak lolos seleksi'
    
print('Nama:', nama)
print('Umur:', umur)
print('Tinggi badan:', tinggi)
print('Berat badan:', berat)
print('Riwayat penyakit:', penyakit)
print('Hasil seleksi:',hasil)