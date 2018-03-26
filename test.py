import os
from xml.etree.ElementTree import ElementTree, dump
from xml.dom import minidom

jenis_kendaraan = []
def get_xml_files(path):
    xml_list = []
    for filename in os.listdir(path):
        if filename.endswith(".xml"):
            xml_list.append(os.path.join(path, filename))
    return xml_list
xml_file_list = get_xml_files("./")

for i in xml_file_list:
    tree = ElementTree()
    tree.parse(i)
    items = tree.findall("filename")
    f2write = open("../test/"+i[2:],"w+")
    for j in items:
        x = i[2:-4]
        y = j.text[:-4]
        if x != y:
            print "tidak ok"
        else:
            print "oke"
        j.text = i[2:-4]+".jpg"
    tree.write(f2write)
