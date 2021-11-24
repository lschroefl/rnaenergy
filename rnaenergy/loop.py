def loop():
    """
    energy values for all kinds of loops
    """
    import numpy
    import importlib_resources

    file = importlib_resources.open_text("energytable", "loop.txt", encoding='utf-8', errors='strict')

    line = file.readline()
    mydict = {}
    while line != "":
        while "----" not in line:
            line = file.readline()
        if "----" in line:
            line = file.readline()
            while line != "":
                line = line.replace("\n", "")
                line = line.split(" ")
                line = list(filter(None, line))
                
     #created a list from the readout of my loop.txt file
     #replace all "." by "0.0"
                g=0
                for i in line:
                    if line[g] == ".":
                        line[g]=0
                        line[g]=float(line[g])

                    # adds the number of bases and the type of loop as the two keys to "mydict"
                        if g == 1:
                            mydict[line[0], "Internal"] = line[g]
                        

                    else:
                        line[g] = float(line[g])


                    if g == 1:
                        mydict[line[0], "Internal"] = line[g]
                    if g == 2:
                        mydict[line[0], "Bulge"] = line[g]
                    if g == 3:
                        mydict[line[0], "Hairpin"] = line[g]
                    g=g+1
                
                
                        
                line = file.readline()

        file.close()


        numpy.save('loopdict', mydict, allow_pickle=True)
        stack = numpy.load('loopdict.npy', allow_pickle=True).item()

        
loop()
import numpy
dict = numpy.load('loopdict.npy', allow_pickle=True).item()
print(dict)