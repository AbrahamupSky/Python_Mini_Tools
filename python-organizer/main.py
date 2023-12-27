import os
import shutil

extensions = {
  '.txt': 'documentos',
  '.docx': 'documentos',
  '.pdf': 'documentos',
  '.jpg': 'imagenes',
  '.png': 'imagenes',
  '.exe': 'ejecutables',
  '.dmg': 'ejecutables',
}

default = 'otros'
organize_default_route = '/Users/abrahamup/Downloads'

files = os.listdir(organize_default_route)
for file in files:
  source_file_path = os.path.join(organize_default_route, file)

  if os.path.isfile(source_file_path):
    _, ext = os.path.splitext(file)
    folder_name = extensions.get(ext.lower(), default)

    destination_file_path = os.path.join(organize_default_route, folder_name)

    if not os.path.exists(destination_file_path):
      os.mkdir(destination_file_path)

    shutil.move(source_file_path, destination_file_path)