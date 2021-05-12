#! /Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9
# Shebang ^^ -- to be run on CLI through (file path or just "." if in current directory)/autoRefresh.py

# Uses "os" - for commmands
# Uses "time" - for waiting
import os
import time
# Put files here:
htmlFile = "~/Documents/index.html"
cssFile  = "~/Documents/style.css"
jsFile = "~/Documents/scripts.js"
auxFile = "~/Documents/about.html"

# Creates a fileList
fileList = [htmlFile, cssFile, jsFile]

# Check if file exists
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

# Infinite loop
while True:
    # Gets change times
    HTMLtimeChanged = os.path.getmtime(fileList[0])
    CSStimeChanged = os.path.getmtime(fileList[1])
    JStimeChanged = os.path.getmtime(fileList[2])
    AUXtimeChanged = os.path.getmtime(auxFile)
    # Waits
    time.sleep(0.01)
    # Gets new change times
    NEWHTMLtimeChanged = os.path.getmtime(htmlFile)
    NEWCSStimeChanged = os.path.getmtime(cssFile)
    NEWJStimeChanged = os.path.getmtime(jsFile)
    NEWAUXtimeChanged = os.path.getmtime(auxFile)
    # Compares new change times to old change times
    if NEWHTMLtimeChanged != HTMLtimeChanged or NEWCSStimeChanged != CSStimeChanged or NEWJStimeChanged != JStimeChanged or NEWAUXtimeChanged != AUXtimeChanged:
        # Refreshes
        os.system("""open -a "Safari" ~/Documents/index.html""")
        time.sleep(0.001)
        # Puts cursor/active back onto IDE/text editor
        os.system("""open -a "Visual Studio Code.app"""")
