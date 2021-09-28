from typing import Text
import numpy as np
import cv2
import imghdr

def changeToBinary(data):
    if(type(data)== str):
        return ''.join([format(ord(i),"08b")for i in data])
    elif(type(data)== bytes or type(data)== np.ndarray):
        return[format (i,"08b")for i in data]
    elif(type(data)== int or type(data)== np.uint8):
        return format (data,"08b")
    else:
        raise TypeError("input type not support")

def hiding_Message(image,message):
    n_bytes = image.shape[0] * image.shape[1]

    if (len(message) > n_bytes):
        print("tidak bisa menyisipkan text karena panjang text melebihi kapasitas")
    
    message += "#"
    data_index = 0
    message_binary = changeToBinary(message)
    data_len = len(message_binary)

    for value in image:
        for pixel in value:
            r,g,b = changeToBinary(pixel)
            if(data_index < data_len):
                pixel[0] = int(r[:-1]+message_binary[data_index],2)
                data_index += 1
            if(data_index < data_len):
                pixel[1] = int(g[:-1]+message_binary[data_index],2)
                data_index += 1
            if(data_index < data_len):
                pixel[2] = int(b[:-1]+message_binary[data_index],2)
                data_index += 1
            if data_index > data_len:
                break
    return image
    
def make_New_Image(image, message,filepath):
    new_filename = input("masukan nam file yang baru")
    new_image = hiding_Message(image,message)
    cv2.imwrite(str(new_filename)+"."+imghdr.what(filepath),new_image)

def decode_Image(image):
    binary_data =""
    for value in image:
        for pixel in value:
            r,g,b = changeToBinary(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]

    all_bytes = [binary_data[i:i+8]for i in range (0,len(binary_data),8)]
    decoded_tetx = ""
    for byte in all_bytes:
        decoded_tetx += chr(int(byte,2))
        if (decoded_tetx[-1:] == "#"):
            break
    return decoded_tetx[:-1]



print("pilih menu steganograpy 1. encode 2.decode")
menu = input("Masukan pilihan menu: ")
if(menu == "1"):
    filepath = input("masukan path dan nama gambar: ")
    message = input("Masukan text: ")
    image = cv2.imread(filepath)
    if(imghdr.what(filepath) != "png" and imghdr.what(filepath) != "BMP" ):
        print("format file tidak di dukung")
    else:
        make_New_Image(image,message,filepath)
elif(menu == "2"):
    filepath = input("masukan path dan nama gambar: ")
    image = cv2.imread(filepath)
    if(imghdr.what(filepath) != "png" and imghdr.what(filepath) != "BMP" ):
        print("format file tidak di dukung")
    else:
        Text = decode_Image(image)
        print(Text)
else:
    print("Menu tersebut tidak tersedia")
