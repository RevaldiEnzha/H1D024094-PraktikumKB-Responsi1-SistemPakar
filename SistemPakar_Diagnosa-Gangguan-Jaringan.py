import tkinter as tk
from tkinter import messagebox

# DATA KERUSAKAN & GEJALA
database_kerusakan={
    "Kerusakan Kabel Optik Utama": ["G01", "G02", "G03", "G04"],
    "Kerusakan Kabel Jaringan Indoor": ["G01", "G05", "G06", "G07"],
    "Kerusakan Konektor/Adapter Kabel": ["G01", "G08", "G09", "G10"],
    "Router/Modem Mati Total": ["G11", "G12"],
    "Daya Sinyal Jaringan Tidak Normal": ["G02", "G09", "G13", "G14", "G15", "G16", "G17"],
    "Router/Modem Sudah Usang (>3 Tahun)": ["G02", "G10", "G18", "G19"],
    "Perangkat TV/Receiver Mati Total": ["G20", "G21", "G22", "G23"],
    "Perangkat Tidak Mendukung Layanan Terbaru": ["G24", "G25", "G26", "G27"],
    "Router/Modem Tidak Menyala": ["G01", "G28", "G29", "G30"],
    "Koneksi Internet Terputus dari Router": ["G01", "G31", "G32", "G33", "G34"],
    "Sinyal Router Bermasalah": ["G35", "G36", "G37", "G38", "G39", "G40"],
}

# DAFTAR SEMUA GEJALA
semua_gejala=[
    ("G01", "Apakah terjadi gangguan atau putusnya koneksi internet?"),
    ("G02", "Apakah performa jaringan menurun (koneksi terasa lambat)?"),
    ("G03", "Apakah jumlah atau kekuatan sinyal berkurang?"),
    ("G04", "Apakah kualitas video atau audio saat streaming memburuk?"),
    ("G05", "Apakah ada gangguan saat mengirim atau menerima data?"),
    ("G06", "Apakah intensitas cahaya pada kabel jaringan menurun?"),
    ("G07", "Apakah kabel jaringan terasa panas tidak normal?"),
    ("G08", "Apakah kualitas sinyal secara umum memburuk?"),
    ("G09", "Apakah perangkat gagal melakukan sinkronisasi dengan jaringan?"),
    ("G10", "Apakah adapter atau modem mengalami panas berlebih?"),
    ("G11", "Apakah semua lampu indikator pada router/modem tidak menyala?"),
    ("G12", "Apakah hanya lampu daya dan sinyal utama yang tidak menyala?"),
    ("G13", "Apakah ada gangguan pada sinyal yang diterima perangkat?"),
    ("G14", "Apakah daya jaringan pada perangkat lain juga ikut menurun?"),
    ("G15", "Apakah ada faktor lingkungan yang mungkin memengaruhi (cuaca, suhu)?"),
    ("G16", "Apakah kondisi fisik kabel atau konektor terlihat rusak atau lecet?"),
    ("G17", "Apakah router atau modem terasa sangat panas saat disentuh?"),
    ("G18", "Apakah perangkat tidak mendukung standar jaringan terbaru?"),
    ("G19", "Apakah kondisi fisik perangkat terlihat usang atau rusak?"),
    ("G20", "Apakah tidak ada tampilan gambar pada layar TV?"),
    ("G21", "Apakah tidak ada sinyal atau sinyal sangat lemah pada TV?"),
    ("G22", "Apakah lampu indikator perangkat TV/receiver mati?"),
    ("G23", "Apakah perangkat TV/receiver tidak merespons remote control?"),
    ("G24", "Apakah firmware atau software perangkat belum diperbarui?"),
    ("G25", "Apakah ada layanan atau konten tertentu yang tidak bisa diakses?"),
    ("G26", "Apakah perangkat memiliki keterbatasan dalam mendukung fitur baru?"),
    ("G27", "Apakah ada masalah pada aplikasi yang digunakan?"),
    ("G28", "Apakah sinyal Wi-Fi tidak terdeteksi sama sekali?"),
    ("G29", "Apakah jaringan Wi-Fi tidak muncul di daftar perangkat lain?"),
    ("G30", "Apakah lampu indikator Wi-Fi pada router mati?"),
    ("G31", "Apakah lampu indikator internet pada router mati?"),
    ("G32", "Apakah perangkat tidak bisa terhubung ke jaringan sama sekali?"),
    ("G33", "Apakah tidak bisa mengakses website atau server dari internet?"),
    ("G34", "Apakah muncul pesan error koneksi pada perangkat yang digunakan?"),
    ("G35", "Apakah lampu sinyal utama pada router mati atau tidak menyala?"),
    ("G36", "Apakah lampu sinyal berkedip dengan lambat?"),
    ("G37", "Apakah lampu sinyal berkedip cepat atau dengan pola tidak biasa?"),
    ("G38", "Apakah lampu sinyal bergantian berkedip dengan warna berbeda?"),
    ("G39", "Apakah lampu sinyal berkedip mengikuti pola kode tertentu?"),
    ("G40", "Apakah lampu sinyal hanya berkedip sekali lalu berhenti?"),
]


class AplikasiPakar:
    def __init__(self, root):
        self.root=root
        self.root.title("Sistem Pakar Diagnosa Gangguan Jaringan Internet")
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        self.label_tanya = tk.Label(
            root,
            text="Selamat Datang di Sistem Pakar Diagnosa Gangguan Jaringan Internet",
            font=("Arial", 12),
            wraplength=420,
            justify="center"
        )
        self.label_tanya.pack(pady=20)

        self.btn_mulai = tk.Button(
            root,
            text="Mulai Diagnosa",
            command=self.mulai_tanya
        )
        self.btn_mulai.pack(pady=10)

        self.frame_jawaban = tk.Frame(root)

        self.btn_ya = tk.Button(
            self.frame_jawaban,
            text="YA",
            width=10,
            command=lambda: self.jawab('y')
        )
        self.btn_tidak = tk.Button(
            self.frame_jawaban,
            text="TIDAK",
            width=10,
            command=lambda: self.jawab('t')
        )

        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)

    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget()
        self.frame_jawaban.pack(pady=20)
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            nomor = self.index_pertanyaan + 1
            self.label_tanya.config(text=f"({nomor}/{len(semua_gejala)}) {teks}")
        else:
            self.proses_hasil()

    def jawab(self, respon):
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)
        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    def proses_hasil(self):
        hasil = []
        for kerusakan, syarat in database_kerusakan.items():
            if all(s in self.gejala_terpilih for s in syarat):
                hasil.append(kerusakan)

        if hasil:
            kesimpulan = "\n".join(f"- {k}" for k in hasil)
            pesan = f"Terdeteksi kemungkinan kerusakan:\n\n{kesimpulan}"
        else:
            pesan = "Tidak terdeteksi kerusakan yang cocok.\nSilakan hubungi teknisi jaringan."

        messagebox.showinfo("Hasil Diagnosa", pesan)

        self.frame_jawaban.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Diagnosa selesai. Ingin mengulang?")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("480x220")
    AplikasiPakar(root)
    root.mainloop()