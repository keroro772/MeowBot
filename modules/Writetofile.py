def writefile(filename, list):
    thefile = open(filename, 'w')
    for item in list:
        thefile.write("%s\n" % item)