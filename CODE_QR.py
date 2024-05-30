import qrcode, PIL
from PIL import Image,ImageTk
import tkinter as tk
from tkinter import ttk,messagebox,filedialog

def createQR(*args):
    data = text_entry.get()
    if data:
        img = qrcode.make(data) 
        res_img = img.resize((280,250))
        #Convert To photoimage
        tkimage= ImageTk.PhotoImage(res_img)
        qr_canvas.create_image(0,0,anchor=tk.NW, image=tkimage)
        qr_canvas.image = tkimage
    else:
        messagebox.showwarning("Warning",'Enter Data in Entry First')

def saveQR():
    data = text_entry.get()
    if data:
        img = qrcode.make(data) 
        res_img = img.resize((280,250))
        
        path = filedialog.asksaveasfilename(defaultextension=".png",)
        if path:
            res_img.save(path)
            messagebox.showinfo("Sucess","QR Code is Saved ")
    else:
        messagebox.showwarning("Warning",'Enter Data in Entry First')
    
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("800x600")
root.config(bg='white')
root.resizable(0,0)

cover_image = Image.open("BGQR.png")
cover_image = cover_image.resize((750, 660))
cover_photo = ImageTk.PhotoImage(cover_image)

cover_label = ttk.Label(root, image=cover_photo)
cover_label.place(x=20, y=10, relwidth=1, relheight=1)

frame1 = tk.Frame(root,bd=2,relief=tk.RAISED)
frame1.place(x=250,y=100,width=280,height=350)

frame2 = tk.Frame(root,bd=2,relief=tk.SUNKEN)
frame2.place(x=250,y=350,width=280,height=100)

cover_img = tk.PhotoImage(file="LOGOQR.png")

qr_canvas = tk.Canvas(frame1)
qr_canvas.create_image(0,0,anchor=tk.NW,image=cover_img)
qr_canvas.image = cover_img
qr_canvas.bind("<Double-1>",saveQR)
qr_canvas.pack(fill=tk.BOTH)

text_entry = ttk.Entry(frame2,width=26,font=("Sitka Small",11),justify=tk.CENTER)
text_entry.bind("<Return>",createQR)
text_entry.place(x=5,y=5)

link_label = ttk.Label(frame2, text="Insert Link:", font=("Sitka Small", 10))
link_label.place(x=5, y=5)

text_entry = ttk.Entry(frame2, width=26, font=("Sitka Small", 11), justify=tk.CENTER)
text_entry.bind("<Return>", createQR)
text_entry.place(x=5, y=30)

btn_1 = ttk.Button(frame2, text="Create", width=10, command=createQR)
btn_1.place(x=25, y=70)

btn_2 = ttk.Button(frame2, text="Save", width=10, command=saveQR)
btn_2.place(x=110, y=70)

btn_3 = ttk.Button(frame2, text="Exit", width=10, command=root.quit)
btn_3.place(x=195, y=70)

root.mainloop()