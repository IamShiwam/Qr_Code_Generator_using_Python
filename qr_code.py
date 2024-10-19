import qrcode

# Getting user input for the QR Code
data = input("Enter the link you want to generate a QR code for: ")
qr_color = input("In which color you want your QR Code: ")
box_height = int(input("Please share the height in cm: "))
border_size = int(input("Width Size: "))

# Initializing the QRCode object 
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=box_height,
    border=border_size
)

# Add the data (user input link)
qr.add_data(f"https://" + data)
qr.make(fit=True)

# Creating the image and setting background colors
img = qr.make_image(fill="black", back_color=qr_color)

# Saved the generated QR code as an image
img.save("generated_QRCode.png")

print("The QR code has been generated successfully. Please check the file manager.")


# made by shiwam chouriya 💫
