import qrcode

# Data to encode
data = "https://github.com/atharva-dev1"

# Creating QR code instance
qr = qrcode.QRCode(
    version=1,  # controls size of the QR Code (1 = 21x21)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border (minimum is 4)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Generating  the image
img = qr.make_image(fill_color="black", back_color="white")

# Saving the QR code image
img.save("qrcode.png")

print("QR code generated and saved as qrcode.png")