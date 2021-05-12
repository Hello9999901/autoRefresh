#! /Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9

import os
import time
htmlFile = "/Users/byranhuang/Documents/GitHub/ArtStudio23/index.html"
cssFile  = "/Users/byranhuang/Documents/GitHub/ArtStudio23/style.css"
jsFile = "/Users/byranhuang/Documents/GitHub/ArtStudio23/scripts.js"
auxFile = "/Users/byranhuang/Documents/GitHub/ArtStudio23/about.html"

fileList = [htmlFile, cssFile, jsFile]

for i in fileList:
    if os.path.exists(i):
        print(i + " - good")
    else:
        print ("ERROR, FILE NOT FOUND")
        exit()

if auxFile == "":
    print ("NO AUX FILE detected")
elif os.path.exists(auxFile):
    print (auxFile + " - good")
else:
    print ("ERROR, AUX FILE NOT FOUND")
    exit()

while True:
    HTMLtimeChanged = os.path.getmtime(fileList[0])
    CSStimeChanged = os.path.getmtime(fileList[1])
    JStimeChanged = os.path.getmtime(fileList[2])
    AUXtimeChanged = os.path.getmtime(auxFile)
    time.sleep(0.01)
    NEWHTMLtimeChanged = os.path.getmtime(htmlFile)
    NEWCSStimeChanged = os.path.getmtime(cssFile)
    NEWJStimeChanged = os.path.getmtime(jsFile)
    NEWAUXtimeChanged = os.path.getmtime(auxFile)
    if NEWHTMLtimeChanged != HTMLtimeChanged or NEWCSStimeChanged != CSStimeChanged or NEWJStimeChanged != JStimeChanged or NEWAUXtimeChanged != AUXtimeChanged:
        os.system("""open -a "Safari" /Users/byranhuang/Documents/GitHub/ArtStudio23/about.html""")
        time.sleep(0.001)
        os.system("open -a /Applications/Visual\ Studio\ Code\ -\ Apple\ Silicon.app")
