# use qrcode library
import qrcode
#import the qrcode and Image classes from the qrcode and PIL libraries
def qr_generate(text):      # define a function name
    # import the qrcode library.
    # Then, we define a QRCode object named qr with the specified version, error correction level, box size, and border.
    qr = qrcode.QRCode(version=1.0, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=3)
    qr.add_data(text) #add_data() is a method of the QRCode class in the qrcode library in Python
    qr.make(fit=True) # The make() method of the QRCode class is used to generate the QR code.
    # The fit parameter is used to specify whether the QR code should be automatically resized to fit the data.
    img = qr.make_image(fill_color="purple", back_color="white") #The make_image() method of the QRCode class is used to generate the QR code image.
    img.show() # display the QR code

url = input("Enter your URL: ")  #  the input() function to prompt the user to enter a URL. The entered URL is stored in the url variable.
qr_generate(url) # the qrcode generate accorfding to your given url