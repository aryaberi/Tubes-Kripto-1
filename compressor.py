import PIL
from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilename()
img = PIL.Image.open(file_path)
_height, _width = img.size

img = img.resize((_height,_width), PIL.Image.ANTIALIAS)
save_path = asksaveasfilename()

img.save(save_path+'_compressed.jpg')