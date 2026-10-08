# Sistem-Pencatatan-Nilai-Mahasiswa-Fina-Salsabila-Prasetyo-097
# Penjelasan Program

Program Sistem Pencatatan Nilai Mahasiswa digunakan untuk mencatat dan menampilkan histori nilai mahasiswa. Program menggunakan file JSON sebagai media penyimpanan data. Data yang sudah dimasukkan akan disimpan ke dalam file data_nilai.json, sehingga data tetap tersedia meskipun program ditutup dan dijalankan kembali.

Program ini memiliki tiga menu utama:

1. Lihat Data Nilai

Menampilkan seluruh data nilai mahasiswa yang tersimpan di file JSON.

2. Tambah Data Nilai

Digunakan untuk menambahkan data NIM, nama, mata kuliah, dan nilai mahasiswa.

3. Keluar

Menghentikan program.


Fungsi **baca_data()**

Fungsi ini digunakan untuk membaca data dari file data_nilai.json. Jika file belum tersedia, program akan menghasilkan list kosong.

Fungsi **simpan_data(data)***

Fungsi ini digunakan untuk menyimpan data ke file JSON menggunakan json.dump().

Fungsi **tampilkan_data()**

Fungsi ini mengambil data dari file kemudian menampilkan seluruh data nilai mahasiswa.

Fungsi **tambah_data()**

Fungsi ini menerima input NIM, nama, mata kuliah, dan nilai. Data tersebut kemudian dimasukkan ke dalam list menggunakan append() dan disimpan kembali ke file JSON.

**Perulangan while**

Program menggunakan while True agar menu dapat digunakan berulang kali sampai pengguna memilih menu keluar.

# terminal
1. tampilan menu
<img width="322" height="168" alt="image" src="https://github.com/user-attachments/assets/bb32725d-f9af-458f-a3b6-5efef2e1b259" />

2. lihat data nilai
<img width="440" height="280" alt="image" src="https://github.com/user-attachments/assets/1acb79a6-7294-49e0-86f2-6ab2276df591" />

3. tambah data
<img width="477" height="360" alt="image" src="https://github.com/user-attachments/assets/dbdc1ecf-fd35-47d9-9813-5e6795d31f3b" />
