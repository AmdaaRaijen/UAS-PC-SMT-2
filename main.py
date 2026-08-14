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


class TabelHashNIM:
    def __init__(self, ukuran=10):
        self.ukuran = ukuran
        self.tabel = [None] * ukuran
 
    def hitung_index(self, nim):
        return nim % self.ukuran
 
    def insert_nim(self, nim):
        index_awal = self.hitung_index(nim)
        index_sekarang = index_awal
 
        for _ in range(self.ukuran):
            if self.tabel[index_sekarang] is None:
                self.tabel[index_sekarang] = nim
                print(f"NIM {nim} disimpan pada index {index_sekarang}")
                return True
            if self.tabel[index_sekarang] == nim:
                print(f"NIM {nim} sudah ada pada index {index_sekarang}")
                return False
            index_sekarang = (index_sekarang + 1) % self.ukuran
 
        print("Hash table penuh, gagal menyimpan NIM", nim)
        return False
 
    def search_nim(self, nim):
        index_awal = self.hitung_index(nim)
        index_sekarang = index_awal
 
        for _ in range(self.ukuran):
            if self.tabel[index_sekarang] is None:
                return None
            if self.tabel[index_sekarang] == nim:
                return index_sekarang
            index_sekarang = (index_sekarang + 1) % self.ukuran
 
        return None
 
    def tampilkan_tabel(self):
        print("\nIsi Hash Table:")
        for index in range(self.ukuran):
            isi = self.tabel[index] if self.tabel[index] is not None else "-"
            print(f"Index {index} : {isi}")
 
 
tabel_hash_nim = TabelHashNIM(ukuran=10)
for mahasiswa in daftar_mahasiswa:
    tabel_hash_nim.insert_nim(mahasiswa["nim"])
 
 
def jalankan_menu_hashing():
    print("\n1. Insert NIM")
    print("2. Search NIM")
    print("3. Tampilkan Hash Table")
    pilihan = input("Pilih aksi: ").strip()
 
    if pilihan == "1":
        nim_input = input("Masukkan NIM baru: ").strip()
        if nim_input.isdigit():
            tabel_hash_nim.insert_nim(int(nim_input))
        else:
            print("NIM harus berupa angka.")
 
    elif pilihan == "2":
        nim_input = input("Masukkan NIM yang dicari: ").strip()
        if nim_input.isdigit():
            hasil_index = tabel_hash_nim.search_nim(int(nim_input))
            if hasil_index is not None:
                print(f"Data ditemukan pada index {hasil_index}")
            else:
                print("Data tidak ditemukan")
        else:
            print("NIM harus berupa angka.")
 
    elif pilihan == "3":
        tabel_hash_nim.tampilkan_tabel()
 
    else:
        print("Pilihan tidak valid.")

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
            jalankan_menu_hashing()
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