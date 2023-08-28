from PIL import Image
import os

downloadsFolder = '/Users/abrahamup/Downloads/LANDrop/' #Ruta de la carpeta de descargas

if __name__ == '__main__':
  for filename in os.listdir(downloadsFolder):
    name, extension = os.path.splitext(downloadsFolder + filename)

    if extension in ['.jpg', '.jpeg', '.png']:
      img = Image.open(downloadsFolder + filename)
      img.save(downloadsFolder + 'compressed_' + filename, optimize=True, quality=60)