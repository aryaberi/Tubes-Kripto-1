from Steganography import encrib, make_New_Image,decode_Image
from tkinter import *
from tkinter import filedialog
import cv2

main = Tk()
main.geometry('500x800+100+200')
plain = Label(main)
Label1 = Label(main)
fileLabel = Label(main)
encrip = Label(main)
Label2 = Label(main)

m = IntVar()
mrd1 = Radiobutton(main,text="Sequencial" ,variable=m, value = 1)
mrd2 = Radiobutton(main,text="Acak", variable=m, value = 2)
mrd3 = Radiobutton(main,text="encript Sequencial" ,variable=m, value = 3)
mrd4 = Radiobutton(main,text=" encript Acak", variable=m, value = 4)


label = Label(main, text = "Masukan Text")
entry = Entry(main,width=30)


label2 = Label(main, text = "Masukan Key")
entry2 = Entry(main,width=30)

label3 = Label(main, text = "Masukan nama file yang baru")
entry3 = Entry(main,width=30)


label4 = Label(main, text = "Masukan Key")
entry4 = Entry(main,width=30)

def pilihFile():
    global fileLabel,path_content,image_content 
    main.filename = filedialog.askopenfilename(initialdir="/c",title="Pilih file")
    fileLabel=Label(main,text=main.filename)
    fileLabel.pack_forget()
    fileLabel.pack()
    fileLabel.place(x=220)
    image = cv2.imread(main.filename)
    path_content = main.filename
    image_content = image

def pilihFile2():
    global fileLabel,path_content,image_content 
    main.filename = filedialog.askopenfilename(initialdir="/c",title="Pilih file")
    fileLabel=Label(main,text=main.filename)
    fileLabel.pack_forget()
    fileLabel.pack()
    fileLabel.place(x=220,y=250)
    image = cv2.imread(main.filename)
    path_content = main.filename
    image_content = image

openFile = Button(main, text="Pilih File", command=pilihFile)
openFile2 = Button(main, text="Pilih File", command=pilihFile2)

def encode(metode,image,filepath,message,key, nama):
    global plain,Label1,encrip,Label2
    Value = make_New_Image(image,message,filepath,metode,nama,key)
    plain.pack_forget()
    Label1.pack_forget()
    Label1 = Label(main, text = "Penyisipan text berhasil, berikut nilai PNSR nya: ")
    Label1.pack()
    Label1.place(x=220,y=20)
    plain = Label(main, text = Value)
    plain.pack()
    plain.place(x=500,y=20)
    if(metode == 3 or metode == 4):
        text = encrib(message)
        encrip.pack_forget()
        Label2.pack_forget()
        Label1 = Label(main, text = "Text telah di encrypht menjadi: ")
        Label1.pack()
        Label1.place(x=220,y=40)
        plain = Label(main, text = text)
        plain.pack()
        plain.place(x=400,y=40)


def decode(image,key):
        global plain,Label1
        Text = decode_Image(image,key)
        plain.pack_forget()
        Label1.pack_forget()
        Label1 = Label(main, text = "Ini Text nya: ")
        Label1.pack()
        Label1.place(x=220,y=270)
        plain = Label(main, text = Text)
        plain.pack()
        plain.place(x=300,y=270)
    
button1 = Button(main, text="Run", command=lambda : encode(m.get(),image_content,path_content,entry.get(),entry2.get(),entry3.get()))
button2 = Button(main, text="Run", command=lambda : decode(image_content,entry4.get()))

judul = Label(main,text="Sisipkan Pesan")
judul.pack
judul.place(x=40,y=0)
mrd1.pack()
mrd1.place(x=40,y=20)
mrd2.pack()
mrd2.place(x=140,y=20)
mrd3.pack()
mrd3.place(x=40,y=40)
mrd4.pack()
mrd4.place(x=160,y=40)



label.pack()
label.place(x=40,y=60)
entry.pack(ipady=5)
entry.place(x=40,y=90)
label2.pack()
label2.place(x=40,y=110)
entry2.pack(ipady=5)
entry2.place(x=40,y=140)
label3.pack()
label3.place(x=40,y=160)
entry3.pack(ipady=5)
entry3.place(x=40,y=190)
openFile.pack()
openFile.place(x=40,y=210)
button1.pack()
button1.place(x=40,y=240)
judul2 = Label(main,text="Tampilkan Pesan")
judul2.pack
judul2.place(x=40,y=280)
label4.pack()
label4.place(x=40,y=300)
entry4.pack(ipady=5)
entry4.place(x=40,y=320)
openFile2.pack()
openFile2.place(x=40,y=340)
button2.pack()
button2.place(x=40,y=370)

main.mainloop()