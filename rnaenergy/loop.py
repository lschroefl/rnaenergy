# reading values of hairpin loop

def loop():
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
                
     #Den ganzen mist als liste dargestellt jetzt ersetze ich noch alle '.' durch 0.0
    #
                g=0
                for i in line:
                    if line[g] is ".":
                        line[g]=0
                        line[g]=float(line[g])

                    #Jetzt erstelle ich ein dictionary dass als keys die basenanzahl und die art der schleife zuordnet
                        if g == 1:
                            mydict[line[0], "Internal"] = line[g]
                        
                            
                            

                        #g=g+1
                        
                    else:
                        line[g] = float(line[g])
                        #line[g]=int(line[g])



                        #g=g+1

                    if g == 1:
                        mydict[line[0], "Internal"] = line[g]
                    if g == 2:
                        mydict[line[0], "Bulge"] = line[g]
                    if g == 3:
                        mydict[line[0], "Hairpin"] = line[g]
                    g=g+1
                
                
                        
                #print(line)          
                line = file.readline()
        #print(mydict)

        file.close()


        numpy.save('loopdict', mydict, allow_pickle=True)
        stack = numpy.load('loopdict.npy', allow_pickle=True).item()


loop()
import numpy
dic = numpy.load('loopdict.npy', allow_pickle=True).item()
print(dic)
            
        
