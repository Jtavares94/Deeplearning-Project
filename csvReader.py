import urllib.request as req
import urllib
import csv

i = 0 
imageurl = "https://lh3.googleusercontent.com/-q8B91vDIQZY/WM-q-ZAfhDI/AAAAAAAAGYw/wr1Cn1kzSCkC5uX_zbkGyn7pYzCzng6dgCOcB/s1600/"
#req.urlretrieve(imageurl, "Deeplearning-Project/images/test.jpg")

# C:\Users\Kevin\Documents\GitHub\Project AI\Deeplearning-Project
with open('C:/Users/Kevin/Desktop/Landmarks/CSV/test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)    
    for row in reader:
        if i < 15:
            i += 1
            image = str(row[1])
            if image == "None":
                print("none")
            else:
                try:
                    id = str(row[0])
                    req.urlretrieve(
                        image, "C:/Users/Kevin/Documents/GitHub/Project AI/Deeplearning-Project/images/" + id + ".jpg")
                except urllib.error.HTTPError as err:
                    if err.code == 403:
                        print("error code: 403")
                    else:
                        print("error")

                # print(image)
