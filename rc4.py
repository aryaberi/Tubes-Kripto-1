# msg = plaintext, key = kunci, n = mode byte (0 - 256)

from numpy import string_


def encr(msg,key,n):
    # print(n)
    # Initiate S
    S = []
    for i in range(2**n):
        S.append(i)
    # print('S: ',S)

    # handle key
    k = list(key) 
    if (len(k) < len(S)):
        for i in range(len(S) - len(k)):
            k.append(k[i % len(k)])
    
    for i in range(len(k)):
        k[i] = ord(k[i])
    # print('k: ',k)
    
    # plain teks but array decimal
    plain = []
    for i in range(len(msg)):
        plain.append(ord(msg[i]))
    # print('plain: ',plain)

    # permutasi
    j = 0
    for i in range(len(S)):
        j = (j + S[i] + k[i]) % len(S)
        # print('j: ',j)
        S[i], S[j] = S[j], S[i]
        # print('iterasi ke -',i)
        # print('S : ',S)

    # pseudorandom bytestream / keystream
    keystream = []
    j = 0
    i = 0
    for m in range(len(plain)):
        i = (i + 1) % len(S)
        j = (j + S[i]) % len(S)
        S[i], S[j] = S[j], S[i]
        # print(S)
        t = (S[i] + S[j]) % len(S)
        keystream.append(S[t])
    # print('keystream: ',keystream)

    # XOR
    cipher = []
    for i in range(len(plain)):
        cipher.append(keystream[i] ^ plain[i])
    # print(cipher)

    # convert to ascii
    for i in range(len(cipher)):
        cipher[i] = chr(cipher[i])
    print(cipher)
    
    string = ""
    for i in range(len(cipher)):
        string += cipher[i]
    return string

# enkripsi dan dekripsi sama karena rc4 itu symmetric
def decr(msg,key,n):
    # Initiate S
    S = []
    for i in range(2**n):
        S.append(i)
    # print('S: ',S)

    # handle key
    k = list(key) 
    if (len(k) < len(S)):
        for i in range(len(S) - len(k)):
            k.append(k[i % len(k)])
    
    for i in range(len(k)):
        k[i] = ord(k[i])
    # print('k: ',k)
    
    # plain teks but array decimal
    plain = []
    for i in range(len(msg)):
        plain.append(ord(msg[i]))
    # print('plain: ',plain)

    # permutasi
    j = 0
    for i in range(len(S)):
        j = (j + S[i] + k[i]) % len(S)
        # print('j: ',j)
        S[i], S[j] = S[j], S[i]
        # print('iterasi ke -',i)
        # print('S : ',S)

    # pseudorandom bytestream / keystream
    keystream = []
    j = 0
    i = 0
    for m in range(len(plain)):
        i = (i + 1) % len(S)
        j = (j + S[i]) % len(S)
        S[i], S[j] = S[j], S[i]
        # print(S)
        t = (S[i] + S[j]) % len(S)
        keystream.append(S[t])
    # print('keystream: ',keystream)

    # XOR
    result = []
    for i in range(len(plain)):
        result.append(keystream[i] ^ plain[i])
    # print(result)

    # convert to ascii
    for i in range(len(result)):
        result[i] = chr(result[i])
    print(result)
    string = ""
    for i in range(len(result)):
        string += result[i]
    return result

# def main():
#     msg = input('Masukkan pesan plain teks: ')
#     key = input('masukkan kunci: ')
#     n = int(input('masukkan n: '))
#     decr(msg,key,n)

# if __name__ == '__main__':
#     main()
    