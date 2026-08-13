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
            # todo: show data
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