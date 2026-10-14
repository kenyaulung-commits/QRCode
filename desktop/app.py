import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
import io

def generate_qr(*args):
    text = entry.get().strip()
    if not text:
        qr_label.config(image='')
        qr_label.image = None
        return
    
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=7,
            border=3,
        )
        qr.add_data(text)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert PIL image to PhotoImage for Tkinter display
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        pil_img = Image.open(img_byte_arr)
        tk_img = ImageTk.PhotoImage(pil_img)
        
        qr_label.config(image=tk_img)
        qr_label.image = tk_img
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR code: {e}")

def clear_input():
    entry.delete(0, tk.END)
    qr_label.config(image='')
    qr_label.image = None

# Initialize main window
root = tk.Tk()
root.title("QR Generator")
root.geometry("380x480")
root.resizable(False, False)

# Header
title_label = tk.Label(root, text="QR Code Generator", font=("Segoe UI", 16, "bold"))
title_label.pack(pady=(20, 10))

# Input Field
entry_frame = tk.Frame(root)
entry_frame.pack(fill="x", padx=30, py=5)

entry_label = tk.Label(entry_frame, text="Enter text or URL:", font=("Segoe UI", 10))
entry_label.pack(anchor="w")

entry = tk.Entry(entry_frame, font=("Segoe UI", 11))
entry.pack(fill="x", py=5)
entry.bind("<KeyRelease>", generate_qr)

# Clear Button
btn_frame = tk.Frame(root)
btn_frame.pack(py=10)

clear_btn = tk.Button(btn_frame, text="Clear & Start Over", command=clear_input, font=("Segoe UI", 9))
clear_btn.pack()

# Display Area
qr_frame = tk.Frame(root, width=260, height=260, bd=1, relief="solid")
qr_frame.pack(pady=15)
qr_frame.pack_propagate(False)

qr_label = tk.Label(qr_frame)
qr_label.pack(expand=True)

root.mainloop()
