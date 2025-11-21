import qrcode

data = input("Enter the text or URL: ").strip()
filename = input("Enter the filename: ").strip()

qr_code = qrcode.QRCode(box_size=10, border=4)
qr_code.add_data(data)

image = qr_code.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f"QRCode saved as {filename}")