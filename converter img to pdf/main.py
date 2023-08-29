import os
from PIL import Image

output_dir = './pdfs/'
input_dir = './images/'

for file in os.listdir(input_dir):
  if file.split('.')[-1] in ('jpg', 'jpeg', 'png'):
    img = Image.open(os.path.join(input_dir, file))
    img_converted = img.convert('RGB')
    img_converted.save(os.path.join(output_dir, '{0}.pdf'.format(file.split('.')[-2])))