import tkinter as tk
from tkinter import messagebox

# Fungsi ini untuk menghitung rata-rata nilai dan menentukan prodi berdasarkan rata-rata
def hasil_prediksi():
    try:
        total_nilai = 0  # Inisialisasi total nilai
        # Loop untuk mengecek setiap input nilai
        for entry in entries:
            # Ambil nilai dari input dan ubah jadi angka
            nilai = int(entry.get())
            # Cek apakah nilai dalam rentang 0 sampai 100
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
            total_nilai += nilai  # Tambahkan nilai ke total

        # Hitung rata-rata nilai
        rata_rata = total_nilai / len(entries)
        
        # Tentukan prodi berdasarkan rata-rata nilai
        if rata_rata >= 80:
            prodi = "Teknologi Informasi"
        elif 60 <= rata_rata < 80:
            prodi = "Pendidikan Bahasa"
        elif 50 <= rata_rata < 60:
            prodi = "Pertanian"
        else:
            prodi = "Tidak ada prodi yang cocok"
        
        # Tampilkan hasil prediksi prodi dan rata-rata nilai
        hasil_label.config(text=f"Prediksi Prodi: {prodi} (Rata-rata: {rata_rata:.2f})")
        
    except ValueError as ve:
        # Jika ada kesalahan, tampilkan pesan error
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Buat jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Judul jendela
root.geometry("500x600")  # Ukuran jendela
root.configure(bg="#f0f0f0")  # Warna latar belakang jendela

# Label untuk judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#f0f0f0")
judul_label.pack(pady=20)  # Tempatkan judul dengan sedikit jarak di atas

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)  # Tempatkan frame dengan jarak di atas

entries = []  # List untuk menyimpan input nilai
for i in range(10):
    # Buat label untuk setiap mata pelajaran
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12), bg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  # Tempatkan label dalam grid
    # Buat kotak input untuk nilai
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)  # Tempatkan kotak input dalam grid
    entries.append(entry)  # Simpan kotak input ke dalam list

# Tombol untuk menghasilkan prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#8645ca", fg="black")
prediksi_button.pack(pady=30)  # Tempatkan tombol dengan jarak di atas

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="blue", bg="#f0f0f0")
hasil_label.pack(pady=20)  # Tempatkan label hasil dengan jarak di atas

# Jalankan aplikasi Tkinter
root.mainloop()