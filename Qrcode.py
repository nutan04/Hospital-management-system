!pip install qrcode

!pip install image

import qrcode
import image

qr=qrcode.QRCode(
version=15,
box_size= 10,
border= 5
)

data="https://www.youtube.com/watch?v=6XmDdIRmg84&t=76s"

qr.add_data(data)

qr.make(fit=True)

img=qr.make_image(fill="back",back_color="white")

img.save("test.png")

img.show("test.png")

