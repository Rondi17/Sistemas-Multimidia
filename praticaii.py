from urllib.request import urlopen
from PIL import Image 
import math

def criarImagemRGB():
    img = Image.new( "RGB", (512,512))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            raster[i,j] = (220,219,97,255)
    (r, g, b) = img.getpixel((0, 0))
    print(r, g, b)
    return img

def criarImagemCinza():
    img = Image.new( "L", (256,512))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            raster[i,j] = i
    y = img.getpixel((5, 5))
    print(y)
    return img

def criarImagemBinaria():
    # checkerboard pattern.
    img = Image.new("1", (250,150))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if ((int(i/25)+int(j/25)) % 2 == 0):
                raster[i,j] = 255
            else:
                raster[i,j] = 0
    y = img.getpixel((0, 0))
    print(y)
    return img

def espelharImg(img):
    #mode, size, color
    x, y = img.size[0], img.size[1]
    new_img = Image.new(img.mode, (x, y))
    raster = img.load()
    raster_new = new_img.load()
    for i in range(x):
        for j in range(y):
            raster_new[x-i-1, j] = raster[i, j]
    return new_img

def reduzirImg(img):
    x, y = img.size[0], img.size[1]
    new_img = Image.new(img.mode, (int(x/2), int(y/2)))
    raster = img.load()
    raster_new = new_img.load()
    for i in range(int(x/2)):
        for j in range(int(y/2)):
            raster_new[i, j] = raster[i*2, j*2]
    return new_img

def transformarCinza(img):
    x, y = img.size[0], img.size[1]
    new_img = Image.new("L", (x, y))
    raster_new = new_img.load()
    for i in range(int(x)):
        for j in range(int(y)):
            (r, g, b) = img.getpixel((i, j))
            tCinza = int((0.3*r+0.59*g+0.11*b))
            raster_new[i, j] = tCinza
    return new_img

def transformarBin(img):
    x, y = img.size[0], img.size[1]
    new_img = Image.new("1", (x, y))
    raster_new = new_img.load()
    for i in range(int(x)):
        for j in range(int(y)):
            (r, g, b) = img.getpixel((i, j))
            tCinza = int((0.3*r+0.59*g+0.11*b))
            if tCinza >= 127:
                raster_new[i, j] = 255
            else:
                raster_new[i, j] = 0
    return new_img

def transformarRed(img):
    x, y = img.size[0], img.size[1]
    new_img = Image.new("RGB", (x, y))
    raster_new = new_img.load()
    for i in range(int(x)):
        for j in range(int(y)):
            (r, g, b) = img.getpixel((i, j))
            raster_new[i, j] = (r, 0, 0, 255)
    return new_img

def transformarGreen(img):
    x, y = img.size[0], img.size[1]
    new_img = Image.new("RGB", (x, y))
    raster_new = new_img.load()
    for i in range(int(x)):
        for j in range(int(y)):
            (r, g, b) = img.getpixel((i, j))
            raster_new[i, j] = (0, g, 0, 255)
    return new_img

def transformarBlue(img):
    x, y = img.size[0], img.size[1]
    new_img = Image.new("RGB", (x, y))
    raster_new = new_img.load()
    for i in range(int(x)):
        for j in range(int(y)):
            (r, g, b) = img.getpixel((i, j))
            raster_new[i, j] = (0, 0, b, 255)
    return new_img

if __name__ == "__main__":
    # Leitura de uma imagem
    img = Image.open(urlopen("https://www.inf.ufsc.br/~roberto.willrich/INE5431/RGB1.jpg"))
    print(img.getpixel((0, 0)))

    # apresentação da imagem
    #img.show()

    # Cria e apresenta uma imagem True Color
    #criarImagemRGB().show()

    #Cria e apresenta uma imagem Tons de Cinza
    #criarImagemCinza().show()

    #Cria e apresenta uma imagem Binária
    #criarImagemBinaria().show()

    #1.
    #espelharImg(img).show()

    #2.
    #reduzirImg(img).show()

    #3.
    #transformarCinza(img).show()

    #4.
    #transformarBin(img).show()

    #5.1
    transformarRed(img).show()

    # 5.2
    transformarGreen(img).show()

    # 5.3
    transformarBlue(img).show()