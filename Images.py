from PIL import Image
import glob

image_list = []

images = glob.glob("C:/Users/Kevin/Documents/GitHub/Project AI/Deeplearning-Project/images/*.jpg") 
for image in images:
    #im = Image.open(image)
    # image_list.append(im)
    with open(image, 'rb') as file:
        img = Image.open(file)
        img.show()
        image_list.append(img)

test = 0
for img in image_list:
    test += 1
    print(test)
