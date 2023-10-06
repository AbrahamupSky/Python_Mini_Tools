from flet import *
from io import BytesIO

import qrcode
import base64

def morning(s):
  qr = qrcode.make(s)
  buffered = BytesIO()
  qr.save(buffered, format = 'JPEG')
  sl = base64.b64encode(buffered.getvalue())
  resultQrCode = sl.decode('utf-8')

  return(resultQrCode)

def main(page: Page):
  # Scroll vertical
  page.scroll = 'always'

  page.vertical_alignment = 'center'
  page.horizontal_alignment = 'center'

  def procedtoCode(e):
    url = morning(txt.value)

    # Generate to img
    img = Image(src_base64=url)

    # If success build to img then add to flet page
    page.add(img)
    page.update()

  # Create text field
  txt = TextField(label='insert to QRCode')

  # Create Btn
  btn = ElevatedButton(
    'Generate QRCode', 
    on_click=procedtoCode,
    bgcolor='blue',
    color='white',
    )
  page.add(txt)
  page.add(btn)

flet.app(target=main)