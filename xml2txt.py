import xml.etree.ElementTree as ET
import os

path = "./"

for f in os.listdir(path):
    object_id = {
        "ban": 1,
        "minibus": 2,
        "mobil": 3,
        "mobilbox": 4,
        "mobilpickup": 5,
        "sedan": 6,
        "tanki": 7,
        "truk": 8,
        "trukmuatan": 9
    }
    if f.endswith(".xml"):
        myxml = ET.parse(f)
        root = myxml.getroot()
        size = root.find("size")
        width = float(size.find("width").text)
        height = float(size.find("height").text)
        for x in root.findall("object"):
            id = object_id[x.find("name").text]-1
            box = x.find("bndbox")
            xmin = box.find("xmin").text
            xmax = box.find("xmax").text
            ymin = box.find("ymin").text
            ymax = box.find("ymax").text
            x_center = ((int(xmax)-int(xmin))/2)+int(xmin)
            x_center /= width
            y_center = ((int(ymax)-int(ymin))/2)+int(ymin)
            y_center /= height
            lebar = int(xmax)-int(xmin)
            lebar /= width
            tinggi = int(ymax)-int(ymin)
            tinggi /= height
            txt = id, x_center,y_center,lebar,tinggi
            print txt
            with open(f[:-3]+"txt","w+") as txtfile:
                txtfile.write(" ".join([str(x) for x in txt])+"\n")
