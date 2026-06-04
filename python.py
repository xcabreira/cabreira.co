import qrcode

img = qrcode.make("https://xcabreira.github.io/cabreira.co/")
img.save("qrcode.png")