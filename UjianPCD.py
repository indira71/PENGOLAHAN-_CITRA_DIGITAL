import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

# fungsi untuk memproses citra dengan metode Transformasi Negatif
def negative_transform(img):
    negative_img = 255 - img
    return negative_img

# fungsi untuk memproses citra dengan metode Median filter
def median_filter(img):
    median_img = cv2.medianBlur(img, 5)
    return median_img

# fungsi untuk menampilkan gambar dalam kotak
def show_image(img, x, y, title):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img)
    label.image = img
    label.place(x=x, y=y)
    title_label = tk.Label(root, text=title)
    title_label.place(x=x, y=y-20)

# fungsi untuk memproses citra dan menampilkan hasilnya
def process_image(method):
    global original_img
    if method == 'negative_transform':
        corrected_img = negative_transform(original_img)
        show_image(corrected_img, 350, 140, 'Hasil Transformasi Negatif')
    elif method == 'median_filter':
        corrected_img = median_filter(original_img)
        show_image(corrected_img, 630, 140, 'Hasil Median Filter')

# fungsi untuk menampilkan informasi pembuat program
def show_creator():
    creator_label = tk.Label(root, text='Nama : Indira Yulianti   | NIM : F55121023   | Kelas : A  | Prodi : Teknik Informatika')
    creator_label.place(x=260, y=480)

# fungsi untuk membuka gambar
def open_image():
    global original_img
    file_path = filedialog.askopenfilename()
    if file_path:
        original_img = cv2.imread(file_path)
        original_img = cv2.resize(original_img, (250, 250))
        show_image(original_img, 70, 140, 'Gambar Original')
        size_label.config(text='Dimensi: {} x {}'.format(original_img.shape[1], original_img.shape[0]))

# membuat jendela utama
root = tk.Tk()
root.geometry('1000x600')
root.title('Aplikasi Pengolahan Citra')

# menambahkan judul gambar original
title_label = tk.Label(root, text='Gambar Original')
title_label.place(x=50, y=20)

# menambahkan tombol untuk membuka gambar
open_button = tk.Button(root, text='Buka Gambar', command=open_image)
open_button.place(x=50, y=50)

# menambahkan label untuk menampilkan dimensi gambar
size_label = tk.Label(root, text='Dimensi: -')
size_label.place(x=150, y=50)

# menambahkan kotak untuk metode perbaikan citra
correction_box = tk.LabelFrame(root, text='Metode Perbaikan Citra', padx=5, pady=5)
correction_box.place(x=350, y=20, width=400, height=70)

# tombol untuk metode Transformasi Negatif
negative_transform_button = tk.Button(correction_box, text='Transformasi Negatif', command=lambda: process_image('negative_transform'))
negative_transform_button.pack(side=tk.LEFT, padx=5)

# tombol
contrast_stretching_button = tk.Button(correction_box, text='Median Filter', command=lambda: process_image('median_filter'))
contrast_stretching_button.pack(side=tk.LEFT, padx=5)

# menambahkan kotak untuk menampilkan hasil perbaikan citra
result_box = tk.LabelFrame(root, text='Hasil Perbaikan Citra', padx=5, pady=5)
result_box.place(x=50, y=100, width=900, height=330)

# menambahkan kotak untuk informasi pembuat program
creator_box = tk.LabelFrame(root, text='Disusun Oleh', padx=5, pady=5)
creator_box.place(x=230, y=450, width=500, height=70)

# menampilkan informasi pembuat program
show_creator()

# menjalankan aplikasi
root.mainloop()
