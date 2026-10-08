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

Fungsi **simpan_data(data)**

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

Pada screenshot ini terlihat program berhasil dijalankan dan menampilkan menu utama. Terdapat tiga pilihan, yaitu:

1. Lihat Data Nilai
2. Tambah Data Nilai
3. Keluar

Menu tersebut digunakan agar pengguna dapat memilih proses yang ingin dilakukan.

2. lihat data nilai
<img width="447" height="302" alt="image" src="https://github.com/user-attachments/assets/2752ad23-7889-4b57-a8ea-87cb2c8f088e" />

Pada screenshot ini terlihat pengguna memilih menu “1. Lihat Data Nilai”. Program kemudian membaca data yang sebelumnya telah disimpan di dalam file data_nilai.json dan menampilkan seluruh data nilai mahasiswa.

Data yang ditampilkan terdiri dari NIM, Nama, Mata Kuliah, dan Nilai. Hal ini menunjukkan bahwa fitur untuk membaca dan menampilkan data dari file JSON telah berhasil berjalan.

Contohnya, data mahasiswa yang ditampilkan adalah:

Nama: agus

NIM: 097

Mata Kuliah: matematika diskrit

Nilai: 85

Dengan adanya tampilan tersebut, pengguna dapat melihat seluruh riwayat nilai mahasiswa yang sudah tersimpan di dalam file.

3. tambah data
<img width="467" height="331" alt="image" src="https://github.com/user-attachments/assets/1a3082bc-23f7-4ecd-acb1-3b29dc294189" />

Pada screenshot ini terlihat pengguna memasukkan data mahasiswa berupa NIM, nama, mata kuliah, dan nilai.

Contoh data yang dimasukkan:

Naman: cinta

NIM: 070

Mata Kuliah: dasar dasar pemograman

Nilai: 85

Setelah semua data dimasukkan, program menampilkan pesan "Data nilai berhasil ditambahkan dan disimpan!". Hal ini menunjukkan bahwa data baru berhasil ditambahkan ke dalam sistem dan disimpan ke file data_nilai.json.

4 keluar

<img width="367" height="175" alt="image" src="https://github.com/user-attachments/assets/334a6c04-efc2-4fd5-8b71-0af2cf7b95f4" />


Pada screenshot ini pengguna memilih menu "3. Keluar". Setelah pilihan tersebut dipilih, program menampilkan pesan "Program selesai." kemudian program berhenti.

Menu keluar digunakan untuk mengakhiri program setelah pengguna selesai melihat atau menambahkan data nilai. Program dapat berhenti karena terdapat perintah break pada bagian menu keluar.

Hal ini menunjukkan bahwa program tidak berjalan terus-menerus tanpa henti, tetapi dapat dihentikan oleh pengguna melalui pilihan menu yang telah disediakan.
