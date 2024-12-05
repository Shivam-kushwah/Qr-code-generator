import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
from io import BytesIO


def generate_qr():
    link = entry.get() 
    if link: 
        try:
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(link)
            qr.make(fit=True)
 
            img = qr.make_image(fill='black', back_color='white')

            img_bytes = BytesIO()
            img.save(img_bytes,format='PNG')
            img_bytes.seek(0)

            with open("qr_code.png","wb") as f:
                f.write(img_bytes.getvalue())
            
            img_tk = ImageTk.PhotoImage(img)
            
            label.config(image=img_tk)
            label.image = img_tk 
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Input Required", "Please enter a valid link!")


root = tk.Tk()
root.title("QR Code Generator")
root.config(bg="#333333")
root.geometry("600x570")
root.resizable(False,False)



label_instructions = tk.Label(root, text="Enter a link to generate QR code:",bg=root.cget("bg"),fg="white",font=("Arial",12))
label_instructions.pack(pady=10)


entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)


button = tk.Button(root, text="Generate QR Code", font=("Arial", 12,"bold"),bg="#2db7e7",fg="white", command=generate_qr,relief="ridge",bd=1)
button.pack(pady=10)


label = tk.Label(root,bg="#333333")
label.pack(pady=20)


root.mainloop()