from rc4 import decr
from imagestegano import make_New_Image,decode_Image
from audiostegano import insertMsg,emitMsg
from tkinter import *
from tkinter import filedialog
import cv2
from rc4 import encr
import imghdr
from compressor import compress

def steganoApp():

    main = Tk()
    main.geometry('500x800+100+200')
    global plain, Label1, fileLabel, encrip, Label2
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

    label5 = Label(main, text = "Masukan nilai n antara 1-256")
    entry5 = Entry(main,width=30)


    label4 = Label(main, text = "Masukan Key")
    entry4 = Entry(main,width=30)

    label6 = Label(main, text = "Masukan nilai n antara 1-256")
    entry6 = Entry(main,width=30)

    def pilihFile():
        global fileLabel,path_content,image_content 
        main.filename = filedialog.askopenfilename(initialdir="/c",title="Pilih file")
        print(imghdr.what(main.filename))
        
        image = cv2.imread(main.filename)
        fileLabel=Label(main,text=main.filename)
        fileLabel.pack_forget()
        fileLabel.pack()
        fileLabel.place(x=220)
        path_content = main.filename
        if(imghdr.what(main.filename)=="png"):
            image_content = compress(image)
            print(image_content.shape)
            print(image.shape)
        else:
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

    def encode(metode,image,filepath,message,key, nama,n):
        global plain,Label1,encrip,Label2
        if n != "":
            n = int(n)
        Value = make_New_Image(image,message,filepath,metode,nama,key,n)
        plain.pack_forget()
        Label1.pack_forget()
        Label1 = Label(main, text = "Penyisipan text berhasil, berikut nilai PNSR nya: ")
        Label1.pack()
        Label1.place(x=220,y=20)
        plain = Label(main, text = Value)
        plain.pack()
        plain.place(x=500,y=20)
        if(metode == 3 or metode == 4):
            text = encr(message,key,n)
            encrip.pack_forget()
            Label2.pack_forget()
            Label1 = Label(main, text = "Text telah di encrypht menjadi: ")
            Label1.pack()
            Label1.place(x=220,y=40)
            plain = Label(main, text = text)
            plain.pack()
            plain.place(x=400,y=40)

    def encode_audio(metode,filepath,message,key,n):
        global plain,Label1,encrip,Label2
        if n != "":
            n = int(n)
        if(metode == 1 or metode == 3):
            isSeq = True
        else:
            isSeq = False
        if metode == 3 or 4:
            text = encr(message,key,n)
        else:
            text = message
        insertMsg(text,filepath,isSeq)
        plain.pack_forget()
        Label1.pack_forget()
        Label1 = Label(main, text = "Penyisipan text berhasil")
        Label1.pack()
        if(metode == 3 or metode == 4):
            encrip.pack_forget()
            Label2.pack_forget()
            Label1 = Label(main, text = "Text telah di encrypht menjadi: ")
            Label1.pack()
            Label1.place(x=220,y=40)
            plain = Label(main, text = text)
            plain.pack()
            plain.place(x=400,y=40)

        
    def decode(image,key,n):
            global plain,Label1
            if n != "":
                n = int(n)
            Text = decode_Image(image,key,n)
            plain.pack_forget()
            Label1.pack_forget()
            Label1 = Label(main, text = "Ini Text nya: ")
            Label1.pack()
            Label1.place(x=220,y=270)
            plain = Label(main, text = Text)
            plain.pack()
            plain.place(x=300,y=270)


    def decode_audio(path,key,n):
            global plain,Label1
            if n != "":
                n = int(n)
            print(key)
            value = emitMsg(path) 
            if key != "":
                text = decr(value,key,n)
            else:
                text = value
            plain.pack_forget()
            Label1.pack_forget()
            Label1 = Label(main, text = "Ini Text nya: ")
            Label1.pack()
            Label1.place(x=220,y=270)
            plain = Label(main, text = text)
            plain.pack()
            plain.place(x=300,y=270)
        
    button1 = Button(main, text="Run Citra", command=lambda : encode(m.get(),image_content,path_content,entry.get(),entry2.get(),entry3.get(),entry5.get()))
    button3 = Button(main, text="Run Audio", command=lambda : encode_audio(m.get(),path_content,entry.get(),entry2.get(),entry5.get()))
    button2 = Button(main, text="Run Citra", command=lambda : decode(image_content,entry4.get(),entry6.get()))
    button4 = Button(main, text="Run Audio", command=lambda : decode_audio(m.get(),path_content,entry4.get(),entry6.get()))

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
    entry3.place(x=40,y=180)
    label5.pack()
    label5.place(x=40,y=200)
    entry5.pack(ipady=5)
    entry5.place(x=40,y=220)
    openFile.pack()
    openFile.place(x=40,y=240)
    button1.pack()
    button1.place(x=40,y=270)
    button3.pack()
    button3.place(x=100,y=270)
    judul2 = Label(main,text="Tampilkan Pesan")
    judul2.pack
    judul2.place(x=40,y=310)
    label4.pack()
    label4.place(x=40,y=330)
    entry4.pack(ipady=5)
    entry4.place(x=40,y=350)
    label6.pack()
    label6.place(x=40,y=370)
    entry6.pack(ipady=5)
    entry6.place(x=40,y=390)
    openFile2.pack()
    openFile2.place(x=40,y=410)
    button2.pack()
    button2.place(x=40,y=440)
    button4.pack()
    button4.place(x=100,y=440)


    main.mainloop()