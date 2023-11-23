import tkinter as tk
import sqlite3

def submit_nilai():
    # Mengambil nilai dari inputan
    nama_siswa = entry_nama.get()
    nilai_biologi = float(entry_biologi.get())
    nilai_fisika = float(entry_fisika.get())
    nilai_inggris = float(entry_inggris.get())

    # Menentukan prediksi berdasarkan nilai tertinggi
    nilai_tinggi = max(nilai_biologi, nilai_fisika, nilai_inggris)
    prediksi_fakultas = ""
    if nilai_tinggi == nilai_biologi:
        prediksi_fakultas = "Kedokteran"
    elif nilai_tinggi == nilai_fisika:
        prediksi_fakultas = "Teknik"
    elif nilai_tinggi == nilai_inggris:
        prediksi_fakultas = "Bahasa"
        


    # Menyimpan data ke SQLite
    conn = sqlite3.connect("D:\Pemrograman Multiplatform\Python1_ SQLite\prodidb.db")
    cursor = conn.cursor()

    # Membuat table jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        nama_siswa TEXT,
                        biologi REAL,
                        fisika REAL,
                        inggris REAL,
                        prediksi_fakultas TEXT
                    )''')

    # Memasukkan data ke dalam table
    cursor.execute("INSERT INTO nilai_siswa VALUES (?, ?, ?, ?, ?)",
                   (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi_fakultas))

    conn.commit()
    conn.close()
    
    

    # Mengosongkan input setelah submit
    entry_nama.delete(0, tk.END)
    entry_biologi.delete(0, tk.END)
    entry_fisika.delete(0, tk.END)
    entry_inggris.delete(0, tk.END)

# Membuat GUI Tkinter
root = tk.Tk()
root.title("Input Nilai Siswa")

# Membuat label dan entry widget untuk input nilai
tk.Label(root, text="Nama Siswa:").pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

tk.Label(root, text="Nilai Biologi:").pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

tk.Label(root, text="Nilai Fisika:").pack()
entry_fisika = tk.Entry(root)
entry_fisika.pack()

tk.Label(root, text="Nilai Inggris:").pack()
entry_inggris = tk.Entry(root)
entry_inggris.pack()

# Membuat button untuk submit nilai
btn_submit = tk.Button(root, text="Submit", command=submit_nilai)
btn_submit.pack()

# Menjalankan loop Tkinter
root.mainloop()
