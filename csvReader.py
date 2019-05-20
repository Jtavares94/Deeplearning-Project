import urllib.request as req
import csv

imageurl = "https://lh3.googleusercontent.com/-q8B91vDIQZY/WM-q-ZAfhDI/AAAAAAAAGYw/wr1Cn1kzSCkC5uX_zbkGyn7pYzCzng6dgCOcB/s1600/"
req.urlretrieve(imageurl, "Deeplearning-Project/images/test.jpg")

with open('D:/HBO/Jaar 3/Minor/Data/test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  next(reader)
  for row in reader:
    image = str(row[1])
    if image == "None":
      print("none")
    else:
      id = str(row[0])
      req.urlretrieve(image, "Deeplearning-Project/images/" + id + ".jpg")
      #print(image)
  

    