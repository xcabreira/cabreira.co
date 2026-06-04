import qrcode

img = qrcode.make("https://www.exemplo.com")
img.save("qrcode.png")