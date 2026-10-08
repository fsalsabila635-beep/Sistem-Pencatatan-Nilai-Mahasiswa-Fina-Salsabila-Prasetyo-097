import json


path = r"C:\Users\TUF\OneDrive\文档\ddp semester1\kasus\kasus6.json"


while True:
    print("\n======================================")
    print("   SISTEM PENCATATAN NILAI MAHASISWA")
    print("======================================")
    print("1. Lihat Data Nilai")
    print("2. Tambah Data Nilai")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    # Menu 1: Membaca dan menampilkan data
    if pilihan == "1":

        # Baca isi file
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        print("\n----- DATA NILAI MAHASISWA -----")

        if len(data) == 0:
            print("Belum ada data nilai.")
        else:
            for i, mahasiswa in enumerate(data, start=1):
                print(f"\nData ke-{i}")
                print("Nama        :", mahasiswa["nama"])
                print("NIM         :", mahasiswa["nim"])
                print("Mata Kuliah :", mahasiswa["mata_kuliah"])
                print("Nilai       :", mahasiswa["nilai"])

    # Menu 2: Menambahkan data baru
    elif pilihan == "2":

        print("\n----- TAMBAH DATA NILAI -----")

        nama = input("Masukkan nama mahasiswa : ")
        nim = input("Masukkan NIM            : ")
        mata_kuliah = input("Masukkan mata kuliah    : ")
        nilai = int(input("Masukkan nilai          : "))

        # Data baru
        data_baru = {
            "nama": nama,
            "nim": nim,
            "mata_kuliah": mata_kuliah,
            "nilai": nilai
        }

        # Membaca data lama
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Menambahkan data baru
        data.append(data_baru)

        # Menyimpan kembali ke file JSON
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("\nData nilai berhasil ditambahkan!")

    # Menu 3: Keluar
    elif pilihan == "3":
        print("\nProgram selesai.")
        break

    else:
        print("\nPilihan tidak tersedia.")
        print("Silakan pilih menu (1-3).")