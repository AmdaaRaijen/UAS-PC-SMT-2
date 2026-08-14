# Sistem Pengelolaan Data Mahasiswa 🎓

**Ujian Akhir Semester (UAS) - Struktur Data dan Algoritma (IF206)**

Program ini adalah sistem pengelolaan data mahasiswa berbasis _Command Line Interface_ (CLI). Program dibangun menggunakan **Python 3** dengan menerapkan algoritma **Sorting**, **Searching**, **Hashing**, **Binary Search Tree (BST)**, dan **Graph**.

---

## 👤 Identitas Mahasiswa

- **Nama** : Bintang Triadmaja
- **NIM** : 250401010075
- **Kelas** : IF206
- **Program Studi** : PJJ Informatika S1
- **Universitas** : Universitas Siber Asia

---

## 📋 Fitur Program

| Menu | Fitur | Algoritma / Struktur Data | Bobot |
|------|-------|---------------------------|-------|
| 1 | Tampilkan Data | — | — |
| 2 | Sorting | Selection Sort (IPK descending) | 20% |
| 3 | Searching | Linear Search by NIM | 20% |
| 4 | Hashing | Hash Table + Linear Probing | 20% |
| 5 | Tree | Binary Search Tree (BST) + Inorder Traversal | 20% |
| 6 | Graph | Adjacency List + BFS & DFS | 20% |
| 7 | Keluar | — | — |

---

## 🛠️ Cara Menjalankan Program

### Opsi 1 — Python di Device Pribadi (Direkomendasikan)

**Persyaratan:** Python versi 3.7 atau lebih baru.

Cek apakah Python sudah terinstall:

```bash
python --version
```

Jika belum terinstall, unduh di [https://www.python.org](https://www.python.org) (pilih versi **terbaru**).

**Langkah menjalankan:**

```bash
python main.py
```

---

### Opsi 2 — Online: Replit

> 🔗 [https://replit.com](https://replit.com)

1. Buka Replit dan buat akun gratis (atau login dengan Google)
2. Klik **+ Create Repl**
3. Pilih template **Python**
4. Hapus isi file `main.py` yang ada, lalu paste seluruh kode program
5. Klik tombol **Run ▶**
6. Input diketik di panel **Console** di sebelah kanan

---

### Opsi 3 — Online: Programiz Online Python Compiler

> 🔗 [https://www.programiz.com/python-programming/online-compiler](https://www.programiz.com/python-programming/online-compiler)

1. Buka link di atas
2. Hapus kode default yang ada
3. Paste seluruh kode program
4. Klik **Run**
5. Input diketik di panel output yang muncul di bawah

> ⚠️ **Catatan:** Beberapa online compiler membatasi fitur `input()` interaktif. Jika input tidak terbaca, gunakan **Replit** (Opsi 2) yang lebih handal untuk program berbasis input terminal.

---

### Opsi 4 — Online: GitHub Codespaces

> 🔗 [https://github.com/codespaces](https://github.com/codespaces)

1. Login ke GitHub, buka link di atas
2. Klik **New codespace** → pilih **Blank**
3. Upload file `main.py` ke file explorer di sebelah kiri
4. Buka terminal (`` Ctrl+` ``) lalu jalankan:

```bash
python main.py
```

---

## 🏗️ Struktur Data & Algoritma yang Digunakan

### Sorting — Selection Sort (Descending by IPK)

Mencari elemen terbesar dari sisa array dan menukarnya ke posisi depan, berulang hingga array terurut dari IPK terbesar ke terkecil.

```
Sebelum : [3.75, 3.20, 3.90, 3.45, 3.80]
Sesudah : [3.90, 3.80, 3.75, 3.45, 3.20]
```

### Searching — Linear Search by NIM

Menelusuri setiap elemen dari awal hingga NIM yang dicari ditemukan. Kompleksitas O(n).

```
Input NIM: 231003
→ Cek 231001 ✗ → 231002 ✗ → 231003 ✓ → Data ditemukan
```

### Hashing — Hash Table + Linear Probing

NIM disimpan ke tabel berukuran 10 menggunakan fungsi hash `index = NIM % 10`. Jika terjadi _collision_, slot berikutnya dicoba secara linear.

```
NIM 231003 → 231003 % 10 = 3 → disimpan di index 3
NIM 231001 → 231001 % 10 = 1 → disimpan di index 1
```

### Tree — Binary Search Tree (BST) + Inorder Traversal

Data dimasukkan ke BST, lalu Inorder Traversal (kiri → akar → kanan) menghasilkan urutan data yang terurut ascending.

```
Insert: 50, 30, 70, 20, 40, 60, 80

        50
       /  \
      30   70
     / \  /  \
    20 40 60  80

Inorder: 20 30 40 50 60 70 80
```

### Graph — Adjacency List + BFS & DFS

Hubungan pertemanan direpresentasikan sebagai Adjacency List. BFS menggunakan queue (FIFO), DFS menggunakan rekursi.

```
Andi : Budi, Citra
Budi : Andi, Deni
Citra: Andi, Eka
Deni : Budi, Eka
Eka  : Citra, Deni

BFS dari Andi: Andi → Budi → Citra → Deni → Eka
DFS dari Andi: Andi → Budi → Deni → Eka → Citra
```

---

## 📁 Struktur File

```
├── main.py
└── README.md
```
