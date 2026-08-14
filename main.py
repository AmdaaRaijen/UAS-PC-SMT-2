daftar_mahasiswa = [
    {"nim": 231001, "nama": "Andi", "ipk": 3.75},
    {"nim": 231002, "nama": "Budi", "ipk": 3.20},
    {"nim": 231003, "nama": "Citra", "ipk": 3.90},
    {"nim": 231004, "nama": "Deni", "ipk": 3.45},
    {"nim": 231005, "nama": "Eka", "ipk": 3.80},
]
 
def tampilkan_data_mahasiswa(data_mahasiswa):
    print(f"{'NIM':<10}{'Nama':<10}{'IPK':<5}")
    for mahasiswa in data_mahasiswa:
        print(f"{mahasiswa['nim']:<10}{mahasiswa['nama']:<10}{mahasiswa['ipk']:.2f}")

def urutkan_mahasiswa_berdasarkan_ipk(data_mahasiswa):
    data_terurut = data_mahasiswa.copy()
    jumlah_data = len(data_terurut)
 
    for indeks_awal in range(jumlah_data - 1):
        indeks_ipk_terbesar = indeks_awal
        for indeks_pembanding in range(indeks_awal + 1, jumlah_data):
            if data_terurut[indeks_pembanding]["ipk"] > data_terurut[indeks_ipk_terbesar]["ipk"]:
                indeks_ipk_terbesar = indeks_pembanding
 
        if indeks_ipk_terbesar != indeks_awal:
            data_terurut[indeks_awal], data_terurut[indeks_ipk_terbesar] = (
                data_terurut[indeks_ipk_terbesar],
                data_terurut[indeks_awal],
            )
 
    return data_terurut

def cari_mahasiswa_berdasarkan_nim(data_mahasiswa, nim_dicari):
    for mahasiswa in data_mahasiswa:
        if mahasiswa["nim"] == nim_dicari:
            return mahasiswa
    return None
 
 
def jalankan_menu_searching():
    nim_input = input("Masukkan NIM: ").strip()
    if not nim_input.isdigit():
        print("NIM harus berupa angka.")
        return
 
    nim_dicari = int(nim_input)
    mahasiswa_ditemukan = cari_mahasiswa_berdasarkan_nim(daftar_mahasiswa, nim_dicari)
 
    if mahasiswa_ditemukan:
        print("\nData ditemukan")
        print(f"NIM : {mahasiswa_ditemukan['nim']}")
        print(f"Nama : {mahasiswa_ditemukan['nama']}")
        print(f"IPK : {mahasiswa_ditemukan['ipk']:.2f}")
    else:
        print("\nData mahasiswa tidak ditemukan")
 
 
def jalankan_menu_sorting():
    print("\nData Mahasiswa Setelah Sorting IPK:")
    data_terurut = urutkan_mahasiswa_berdasarkan_ipk(daftar_mahasiswa)
    tampilkan_data_mahasiswa(data_terurut)

def tampilkan_menu_utama():
    print("\n===== MENU PENGELOLAAN DATA MAHASISWA =====")
    print("1. Tampilkan Data")
    print("2. Sorting")
    print("3. Searching")
    print("4. Hashing")
    print("5. Tree")
    print("6. Graph")
    print("7. Keluar")

def main():
    while True:
        tampilkan_menu_utama()
        pilihan_menu = input("Pilih menu: ").strip()
 
        if pilihan_menu == "1":
            print("\nData Mahasiswa:")
            tampilkan_data_mahasiswa(daftar_mahasiswa)
        elif pilihan_menu == "2":
            jalankan_menu_sorting()
        elif pilihan_menu == "3":
            jalankan_menu_searching()
        elif pilihan_menu == "4":
            print("\nHash Table")
            # todo: hash table
        elif pilihan_menu == "5":
            print("\nTree")
            # todo: tree
        elif pilihan_menu == "6":
            print("\nGraph")
            # todo: graph
        elif pilihan_menu == "7":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
 
 
if __name__ == "__main__":
    main()