import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://linktr.ee/MarsExtensions')
qr.make(fit=True)

img = qr.make_image(fill_color=(255, 153, 255), back_color="black")
img.save("mars-pink.png")
