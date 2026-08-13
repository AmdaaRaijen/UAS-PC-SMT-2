def main():
    while True:
        tampilkan_menu_utama()
        pilihan_menu = input("Pilih menu: ").strip()
 
        if pilihan_menu == "1":
            print("\nData Mahasiswa:")
            # todo: show data
        elif pilihan_menu == "2":
            # todo: do shorting
        elif pilihan_menu == "3":
            # todo: searching
        elif pilihan_menu == "4":
            # todo: hash table
        elif pilihan_menu == "5":
            # todo: tree
        elif pilihan_menu == "6":
            # todo: graph
        elif pilihan_menu == "7":
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
 
 
if __name__ == "__main__":
    main()