# autoRefresh

This is a program that automatically refreshes an HTML file when its related files (the HTML itself, CSS, JS, or any other file) is changed.


## How it works:
In simple terms, everytime the modification time for a file changes, the program runs ```open -a "Safari" <html_path>``` to open the file in Safari. It works in other applications by replacing the "Safari" to another app. 

### Nuances:
To "Google Chrome", for example. However, when done through Google Chrome or any other browser that is not Safari, it will open a new tab every time it is supposed to refresh. Only Safari refreshes.


## OS SUPPORT:

 - ```macOS```
 - ```No support for other operating systems yet -- sorry!```


## EXAMPLE:
In the file, there are four string variables:
 - ```htmlFile```
 - ```cssFile```
 - ```jsFile```
 - ```auxFile```
Change these variables above to absolute paths of files. For example,
I can put these (macOS):
```python
htmlFile = "/Users/byranhuang/Documents/GitHub/ArtStudio23/index.html"
cssFile  = "/Users/byranhuang/Documents/GitHub/ArtStudio23/style.css"
jsFile = "/Users/byranhuang/Documents/GitHub/ArtStudio23/scripts.js"
auxFile = "/Users/byranhuang/Documents/GitHub/ArtStudio23/about.html"
```
