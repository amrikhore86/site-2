import pyshorteners

link = input ('Paste your URL : ')
shortener=pyshorteners.Shortener()
x=shortener.tinyurl.short(link)
print(x)