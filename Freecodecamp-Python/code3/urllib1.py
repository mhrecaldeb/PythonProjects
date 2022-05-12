import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt', cadefault= False)
for line in fhand:
    print(line.decode().strip())
