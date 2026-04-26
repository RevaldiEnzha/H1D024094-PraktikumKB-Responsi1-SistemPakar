### Nama: Revaldi Enzha Agviandry P
### NIM: H1D024094
### Shift KRS: C
### Shift Baru: C

# Sistem Pakar Diagnosa Gangguan Jaringan Internet

Program Python berbasis GUI (Tkinter) yang menggunakan pendekatan **sistem pakar** untuk membantu mendiagnosa kemungkinan kerusakan pada jaringan internet rumahan berdasarkan gejala yang dialami pengguna. Program akan menanyakan gejala satu per satu, lalu mencocokkannya dengan knowledge base yang telah tersimpan di dalam sistem.

---

## Struktur Program
### 1. Knowledge Base — `database_kerusakan`

```python
database_kerusakan = {
    "Kerusakan Kabel Optik Utama": ["G01", "G02", "G03", "G04"],
    "Router/Modem Mati Total": ["G11", "G12"],
    ...
}
```

Bagian ini menyimpan basis pengetahuan sistem pakar dalam bentuk dictionary. Setiap *key* adalah nama kerusakan, dan *value*-nya adalah list berisi kode-kode gejala yang **semuanya harus terpenuhi** agar kerusakan tersebut dapat terdeteksi. Struktur ini memisahkan data dari logika program, sehingga knowledge base mudah dikembangkan tanpa mengubah alur program.

---

### 2. Daftar Pertanyaan Gejala — `semua_gejala`

```python
semua_gejala = [
    ("G01", "Apakah terjadi gangguan atau putusnya koneksi internet?"),
    ("G02", "Apakah performa jaringan menurun (koneksi terasa lambat)?"),
    ...
]
```

Berisi **40 pertanyaan gejala** dalam format `(kode_gejala, teks_pertanyaan)`. Kode gejala (G01–G40) menjadi penghubung antara jawaban pengguna dengan aturan kerusakan yang ada pada `database_kerusakan`. Dengan struktur ini, program dapat mengiterasi seluruh pertanyaan secara berurutan tanpa perlu logika tambahan.

---

### 3. Kelas Utama — `AplikasiPakar`

```python
class AplikasiPakar:
    def __init__(self, root):
        ...
```

Seluruh logika GUI dan alur program dikelola dalam satu kelas ini. Pada saat inisialisasi (`__init__`), semua komponen antarmuka dibuat: label pertanyaan, tombol mulai, dan frame tombol YA/TIDAK. Frame tombol jawaban disembunyikan di awal dan baru dimunculkan setelah pengguna menekan tombol Mulai.

---

### 4. Alur Diagnosa — `mulai_tanya()` dan `tampilkan_pertanyaan()`

```python
def mulai_tanya(self):
    self.gejala_terpilih = []
    self.index_pertanyaan = 0
    self.btn_mulai.pack_forget()
    self.frame_jawaban.pack(pady=20)
    self.tampilkan_pertanyaan()

def tampilkan_pertanyaan(self):
    if self.index_pertanyaan < len(semua_gejala):
        kode, teks = semua_gejala[self.index_pertanyaan]
        self.label_tanya.config(text=f"({nomor}/{len(semua_gejala)}) {teks}")
    else:
        self.proses_hasil()
```

Ketika diagnosa dimulai, list `gejala_terpilih` dan index pertanyaan direset ke kondisi awal. Fungsi `tampilkan_pertanyaan()` bekerja setiap kali dipanggil, ia menampilkan pertanyaan sesuai index saat ini. Ketika index sudah melampaui jumlah pertanyaan, fungsi ini otomatis memanggil `proses_hasil()`. Counter `(nomor/total)` ditampilkan agar pengguna mengetahui sejauh mana progress diagnosa.

---

### 5. Pengumpulan Jawaban — `jawab()`

```python
def jawab(self, respon):
    if respon == 'y':
        kode = semua_gejala[self.index_pertanyaan][0]
        self.gejala_terpilih.append(kode)
    self.index_pertanyaan += 1
    self.tampilkan_pertanyaan()
```

Fungsi ini dipanggil setiap kali pengguna menekan tombol YA atau TIDAK. Jika jawabannya YA, kode gejala dari pertanyaan saat ini ditambahkan ke `gejala_terpilih`. Jika TIDAK, tidak ada yang ditambahkan. Setelah itu index dinaikkan dan pertanyaan berikutnya ditampilkan.

---

### 6. Mesin Inferensi — `proses_hasil()`

```python
def proses_hasil(self):
    hasil = []
    for kerusakan, syarat in database_kerusakan.items():
        if all(s in self.gejala_terpilih for s in syarat):
            hasil.append(kerusakan)
```

Inti dari sistem pakar. Fungsi ini mencocokkan fakta yang ada (gejala yang dipilih pengguna) dengan setiap aturan dalam knowledge base. Fungsi `all()` memastikan bahwa **semua gejala yang disyaratkan** oleh suatu kerusakan harus terpenuhi agar kerusakan itu terdeteksi. Karena semua kerusakan diperiksa satu per satu, sistem ini juga dapat mendeteksi **lebih dari satu kerusakan sekaligus** apabila gejala yang dimasukkan memenuhi beberapa aturan sekaligus.

---

## Kerusakan yang Dapat Dideteksi

| No | Kerusakan | Jumlah Gejala yang Diperlukan |
|----|-----------|-------------------------------|
| 1 | Kerusakan Kabel Optik Utama | 4 gejala |
| 2 | Kerusakan Kabel Jaringan Indoor | 4 gejala |
| 3 | Kerusakan Konektor/Adapter Kabel | 4 gejala |
| 4 | Router/Modem Mati Total | 2 gejala |
| 5 | Daya Sinyal Jaringan Tidak Normal | 7 gejala |
| 6 | Router/Modem Sudah Usang (>3 Tahun) | 4 gejala |
| 7 | Perangkat TV/Receiver Mati Total | 4 gejala |
| 8 | Perangkat Tidak Mendukung Layanan Terbaru | 4 gejala |
| 9 | Router/Modem Tidak Menyala | 4 gejala |
| 10 | Koneksi Internet Terputus dari Router | 5 gejala |
| 11 | Sinyal Router Bermasalah | 6 gejala |

---

## Cara Menjalankan

```bash
python sistem_pakar_jaringan.py
```

Tidak memerlukan instalasi library tambahan. Klik **Mulai Diagnosa**, jawab setiap pertanyaan dengan menekan tombol **YA** atau **TIDAK**, dan hasil diagnosa akan muncul setelah semua pertanyaan selesai dijawab.

---

## Requirement

- Python 3.x
- Tkinter (sudah termasuk bawaan Python)
- Tidak memerlukan library tambahan
