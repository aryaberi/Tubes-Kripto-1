# We will use wave package available in native Python installation to read and write .wav audio file
import wave

def swapCouple(arrBits):
    for i in range(len(arrBits)):
        if (i % 2 ==0):
            if(i < (len(arrBits)-1)):
                temp = arrBits[i]
                arrBits[i] = arrBits[i+1]
                arrBits[i+1] = temp
        else:
            continue
    return arrBits

# isSeq represents whether the insertion is sequentially (True) or randomly (False)
def insertMsg(msg, audioPath, isSeq):
    # read wave audio file
    song = wave.open(audioPath, mode='rb')
    # Read frames and convert to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # The "secret" text message
    string = msg
    # If the length of message is bigger than the inserted audio, return error
    if (((len(frame_bytes)-(len(string)*8*8))/8)-1 < 0):
        print('Ukuran Audio tidak cukup menampung semua pesan, proses dibatalkan')
    else:
        # Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.
        string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
        # Convert text to bit array
        bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))
        bits = bits if isSeq else swapCouple(bits)
        bits = [1]+bits if isSeq else [0]+bits

        # Replace LSB of each byte of the audio data by one bit from the text bit array
        for i, bit in enumerate(bits):
            frame_bytes[i] = (frame_bytes[i] & 254) | bit
    
    # Get the modified bytes
    frame_modified = bytes(frame_bytes)

    # Write bytes to a new wave audio file
    with wave.open('audio_embedded.wav', 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    song.close()

def emitMsg(audioPath):
    song = wave.open(audioPath, mode='rb')
    # Convert audio to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    # Extract the LSB of each byte
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    isSeq = extracted[0]
    extracted = extracted[1:]
    extracted = extracted if isSeq else swapCouple(extracted)
    # Convert byte array back to string
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    # Cut off at the filler characters
    decoded = string.split("###")[0]

    # return the extracted text
    song.close()
    return decoded

# insertMsg('Selamat Siang, perkenalkan nama saya Angga halo ASSALAMUALAIKUM?', "sample.wav", True)
# print(emitMsg("audio_embedded.wav"))
