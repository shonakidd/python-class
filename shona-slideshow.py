from PIL import Image
image = Image.open("Photos/morgan1.jpg")
image.show()

import time
 
# Wait for 2 seconds
time.sleep(2)

image = Image.open("Photos/morgan2.jpg")
image.show()

# Wait for 2 seconds
time.sleep(2)

image = Image.open("Photos/nyancat.jpeg")
image.show()