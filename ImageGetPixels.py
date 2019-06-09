from PIL import Image, ImageOps
import glob
import numpy as np

# ####### IMAGE SCALLING #######


images = glob.glob("C:/Users/Kevin/Documents/GitHub/Project AI/Deeplearning-Project/images/*.jpg")
id = 0
pictures = []

#for image in images:
#    original_image = Image.open(image)
#    size = (100, 100)
#    fit_and_resized_image = ImageOps.fit(original_image, size, Image.ANTIALIAS)
#
#    #original_image.show()
#    fit_and_resized_image.show()
#    pictures.append(fit_and_resized_image)


#print(pictures)

for image in images:
    id += 1
    img = Image.open(image).convert('LA')
    size = (100, 100)
    img_resized = ImageOps.fit(img, size, Image.ANTIALIAS)

    #img.save('greyscale' + str(id) + '.png')
    pix_val = list(img_resized.getdata())
    pix_val_flat = [x for sets in pix_val for x in sets]

    print(pix_val_flat)
    #print(np.mean(img))