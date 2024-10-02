import qrcode

data = "https://www.muhammedshamir.in"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = "black",black_color="white")

img.save("image.png")
print("qr code ")