import os

ext = ".jpg"
out = "output.txt"
with open(out,"w+") as txt:
    for f in os.listdir("./"):
        if not f.endswith(ext):
            abspath = os.path.abspath(f)
            txt.write(abspath+"\n")
