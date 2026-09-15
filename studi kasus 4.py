buku = {
    "judul" : "Belajar Pemograman Python",
    "penulis" : "Graceilla Hutagalung",
    "tahun_terbit" : 2024
}
print("Data Buku Awal:")
print(buku)
print()

while True:
    print("==== MENU PENGELOLAAN DATA BUKU ====")   
    print("1. Tampilkan data buku")
    print("2. Tambah data penerbit")
    print("3. Ubah data penulis")
    print("4. Hapus data penerbit")
    print("5. Keluar")

    print("======================================")

    pilihan = input("pilih menu (1-5): ")
    print()

    if pilihan == "1":
        print("--- Data Buku ---")
        print("key:", buku.keys())
        print("Value:", buku.values())
        print("Isi lengkap:", buku)
        print()
    elif pilihan == "2":
        buku["penerbit"] = "Penerbit Informatika"
        print("Setelah tambah penerbit :")
        print(buku)
        print()
    elif pilihan == "3":
        buku.update({"penulis" : "Michalle"})
        print("Setelah ubah penulis:")
        print(buku)
        print()
    elif pilihan == "4":
        buku.pop("penerbit")
        print("Setelah hapus penerbit:")
        print(buku)
        print()
    elif pilihan == "5":
        print("--- Data Buku Akhir ---")
        print(buku)
        print("\nTerima Kasih, program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi. \n")