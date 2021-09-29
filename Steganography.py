from typing import Text
import numpy as np
import cv2
import imghdr
from random import seed, shuffle
from math import log10, sqrt

# untuk mengubah data-data menjadi file Binary 8bit
def changeToBinary(data):
    if(type(data)== str ):
        return ''.join([format(ord(i),"08b")for i in data])
    elif(type(data)== bytes or type(data)== np.ndarray):
        return[format (i,"08b")for i in data]
    elif(type(data)== int or type(data)== np.uint8):
        return format (data,"08b")
    else:
        raise TypeError("input type not support")

#memasukan Text kedalam file
def hiding_Message(image,message,pilihan,key):
    n_bytes = image.shape[0] * image.shape[1]
    Text = ""
    if pilihan == 1:
        Text += "*"
    elif pilihan == 2:
        Text += "@"
    if (len(message) > n_bytes):
        print("tidak bisa menyisipkan text karena panjang text melebihi kapasitas")
    
    Text += message
    Text += "#"
    data_index = 0
    message_binary = changeToBinary(Text)
    data_len = len(message_binary)
    if pilihan == 1:
        for i in range(len(image)):
            for pixel in image[i]:
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
                if data_index >= data_len:
                    break
    if pilihan == 2:
        random = [0]
        place_LSB = PRNG(image,key)
        shuffle(place_LSB)
        new_random = random+place_LSB 
        for i in new_random:
            for pixel in image[i]:
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
                if data_index >= data_len:
                    break
    return image

#membuat file baru yang telah disisipkan text    
def make_New_Image(image, message,filepath,pilihan,new_filename,key):
    new_image = hiding_Message(image,message,pilihan,key)
    value = PSNR(image,new_image)
    cv2.imwrite(str(new_filename)+"."+imghdr.what(filepath),new_image)
    return value

#mendapatkan code image apakah sequencial atau acak
def get_code_Image(image):
    binary_data =""
    for pixel in image[0]:
        r,g,b = changeToBinary(pixel)
        binary_data += r[-1]
        binary_data += g[-1]
        binary_data += b[-1]

    all_bytes = [binary_data[i:i+8]for i in range (0,len(binary_data),8)]
    decoded_tetx = ""
    decoded_tetx += chr(int(all_bytes[0],2))
    return decoded_tetx

#menampilkan tulisan yang disisipkan oleh gambar
def decode_Image(image,key):
    code = get_code_Image(image)
    binary_data =""
    if code == "*":
        for value in image:
            for pixel in value:
                r,g,b = changeToBinary(pixel)
                binary_data += r[-1]
                binary_data += g[-1]
                binary_data += b[-1]
    elif code == "@":
        random = [0]
        place_LSB = PRNG(image,key)
        shuffle(place_LSB)
        new_random = random+place_LSB 
        for i in new_random:
            for pixel in image[i]:
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
    return decoded_tetx[1:-1]

#untuk mengacak
def PRNG(image,key):
    seed(key)
    sequence = [i for i in range(1,len(image))]
    return sequence

#hitung PSNR
def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

