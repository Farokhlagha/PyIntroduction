# Make QRcode with Name and Phone number

import qrcode

name = input("please enter your name: ")
mobile = input("please enter your mobile number: ")

qr_img= qrcode.make(name + mobile)
qr_img.save("qr_code.jpg")