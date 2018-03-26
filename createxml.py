import xml.etree.ElementTree as ET
import xml.dom.minidom as dom
import os
import cv2

path_name = "/home/kmzway87aa/Documents/models/research/object_detection/seleksi/"
folder_name = "seleksi"

for f in os.listdir(path_name):
    if f.endswith(".txt"):
        with open(f) as txt:

            # defining the structure of the xml file
            annotation = ET.Element("annotation")
            folder = ET.SubElement(annotation, "folder")
            filename = ET.SubElement(annotation, "filename")
            path = ET.SubElement(annotation, "path")
            source = ET.SubElement(annotation, "source")
            database = ET.SubElement(source, "database")
            size = ET.SubElement(annotation, "size")
            width = ET.SubElement(size, "width")
            height = ET.SubElement(size, "height")
            depth = ET.SubElement(size, "depth")
            segmented = ET.SubElement(annotation, "segmented")

            # assigning value
            folder.text = folder_name
            filename.text = txt.readline()[:-1] # read line excluding the new line char
            path.text = path_name+filename.text
            database.text = "Unknown"
            segmented.text = "0"
            img = cv2.imread(path.text)
            h, w, d = img.shape
            height.text = str(h)
            width.text = str(w)
            depth.text = str(d)
            objects = []
            count = 0
            for line in txt:
                boxes, n = line[:-1].split(":")
                ymn, xmn, ymx, xmx = boxes.split(", ")
                objects.append(ET.SubElement(annotation, "object"))
                name = ET.SubElement(objects[count], "name")
                pose = ET.SubElement(objects[count], "pose")
                truncated = ET.SubElement(objects[count], "truncated")
                difficult = ET.SubElement(objects[count], "difficult")
                bndbox = ET.SubElement(objects[count], "bndbox")
                xmin = ET.SubElement(bndbox, "xmin")
                ymin = ET.SubElement(bndbox, "ymin")
                xmax = ET.SubElement(bndbox, "xmax")
                ymax = ET.SubElement(bndbox, "ymax")
                name.text = n
                pose.text = "Unspecified"
                truncated.text = "0"
                difficult.text = "0"
                xmin.text = xmn
                ymin.text = ymn
                xmax.text = xmx
                ymax.text = ymx
                count += 1

            xmlstr = ET.tostring(annotation, encoding='utf8', method='xml')
            xmlstr = dom.parseString(xmlstr).toprettyxml()
            with open(filename.text[:-3]+"xml","w+") as xmlfile:
                xmlfile.write(xmlstr)
                print "oke!"
