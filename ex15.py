from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file {file!r}".format(file=filename)
print "file name", txt.name
print txt.read()

txt.close()
