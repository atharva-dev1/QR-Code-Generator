import qrcode as qr
img = qr.make("Hi , How are you?")
img.save("text.png")
