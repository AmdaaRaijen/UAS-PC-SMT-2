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
            # todo: do shorting
            print("\nShorting")
        elif pilihan_menu == "3":
            print("\nSearching")
            # todo: searching
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