# proses dan langkah langkah
## Inisialisasi Data
Data biodata_list berisi beberapa informasi pribadi berupa list yang berisi dictionary untuk setiap individu. Setiap dictionary memiliki data seperti:
nama
umur
tinggi badan
berat badan
riwayat penyakit
## Input Data
Program meminta pengguna untuk memasukkan data pribadi mereka:
nama (string): Nama pengguna.
umur (integer): Umur pengguna.
tinggi (integer): Tinggi badan pengguna.
berat (integer): Berat badan pengguna.
penyakit (string): Riwayat penyakit pengguna.
## Definisi Kriteria Seleksi
Program menentukan persyaratan untuk lolos seleksi:
persyaratan_tinggi_min: 175 cm (tinggi badan minimal).
persyaratan_berat_max: 70 kg (berat badan maksimal).
riwayat_penyakit_tidak_ada: 'tidak ada' (riwayat penyakit harus 'tidak ada').
## Logika Seleksi
Program melakukan pengecekan terhadap data yang dimasukkan pengguna menggunakan kondisi if-else:
Memastikan bahwa:
umur ≤ 20 tahun.
tinggi ≥ persyaratan_tinggi_min (175 cm).
penyakit sama dengan 'tidak ada'.
berat ≤ persyaratan_berat_max (70 kg).
Jika semua kondisi terpenuhi, maka:
hasil = 'Lolos seleksi'.
Jika ada satu atau lebih kondisi yang tidak terpenuhi, maka:
hasil = 'Tidak lolos seleksi'.
## Output Hasil Seleksi
Program menampilkan data pengguna yang dimasukkan dan hasil seleksi:
Nama.
Umur.
Tinggi badan.
Berat badan.
Riwayat penyakit.
Hasil seleksi.