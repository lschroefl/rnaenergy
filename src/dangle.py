def dangleend():
    import os
    import numpy
    from importlib import resources  #used to read resources included in the package
    import io                       #converting bites
    os.chdir("/home/casali/Schreibtisch/6Semester/Bachelorarbeit/NNDB/turner04")
    file = open("dangle.txt", "r")
    # todo stop using a relative path (os.chdir to open .txt files)
    #firstLine= file.readline()
    #secondLine = file.readline()
    #regular expressions (RE)

    D={}

    index = 0

    for i in range(6):
        i = file.readline()
    thumb = "A    C    G    U"
    allValues={}

    line = file.readline()
    while line != "":

        #starting at our constant header "A  C  G  U"
        if thumb in line:

            #skipping unnecessary lines
            while "X" not in line:
                line = file.readline()

            for i in range(1):
                if "X" in line:

                    #line = file.readline()

                    #----------------------------------------------------------------------------------------------5' 3'----------------
                    #creating a list of our bases of interest, of ur 5' to 3' thread, always 2 paired nucleotides
                    a = 0
                    #b = 1
                    l = []
                    z = line.count("X")
                    #print(z)
                    #print(type(l))
                    k = line[a] #+line[b]
                    for i in range (z):
                        line=line.replace(" ", "")
                        line = line.replace("X", "")
                        line = line.replace("Y", "")
                        k=line[a] #+line[b]
                        l.append(k)
                        a=a+1
                        #b=b+2
                    #print(l)


            # Now we are adding 1 nucleotide in the middle of our basepair that we received from list l above. We are doing this 4 times, 1 time for each nucleotide
            #1
            XbaseA= []
            for i in l :
                i=list(i)
                i.insert(1,"A")
                i=str(i)
                i.replace(",", "")
                XbaseA.append(i)
            #print(XbaseA)

            #2
            XbaseC= []
            for i in l :
                i=list(i)
                i.insert(1,"C")
                i=str(i)
                i.replace(",", "")
                XbaseC.append(i)
            #print(XbaseC)

            #3
            XbaseG= []
            for i in l :
                i=list(i)
                i.insert(1,"G")
                i=str(i)
                i.replace(",", "")
                XbaseG.append(i)
            #print(XbaseG)

            #4
            XbaseU= []
            for i in l :
                i=list(i)
                i.insert(1,"U")
                i=str(i)
                i.replace(",", "")
                XbaseU.append(i)
            #print(XbaseU)


            #Going to our next nucleotide pairs of interest
            for i in range(1):
                line=file.readline()

            #print("\n")
            else:

                a = 0
                #b = 1
                l = []
                z = line.count("X")
                #print(z)
                #print(type(l))
                k = line[a] #+line[b]
                for i in range (4):
                    line=line.replace(" ", "")
                    line = line.replace("X", "")
                    line = line.replace("Y", "")
                    k=line[a] #+line[b]
                    l.append(k)
                    a=a+1
                    #b=b+2
                #print(l)


                # Now we are adding 1 nucleotide in the middle of our basepair that we received from list l above. We are doing this 4 times, 1 time for each nucleotide
                #1
                XbaseA= []
                for i in l :
                    i=list(i)
                    #i.insert(1,"A")
                    i=str(i)
                    i.replace(",", "")
                    XbaseA.append(i)
                #print(XbaseA)

                #2
                XbaseC= []
                for i in l :
                    i=list(i)
                    #i.insert(1,"C")
                    i=str(i)
                    i.replace(",", "")
                    XbaseC.append(i)
                #print(XbaseC)

                #3
                XbaseG= []
                for i in l :
                    i=list(i)
                    #i.insert(1,"G")
                    i=str(i)
                    i.replace(",", "")
                    XbaseG.append(i)
                #print(XbaseG)

                #4
                XbaseU= []
                for i in l :
                    i=list(i)
                    #i.insert(1,"U")
                    i=str(i)
                    i.replace(",", "")
                    XbaseU.append(i)
                #print(XbaseU)


                #Going to our next nucleotide pairs of interest
                for i in range(1):
                    line=file.readline()


            #-----------------------------------------------------------------------------------------------3' 5'----------------------------
            #creating the second list of our bases of interest, of our 3' to 5' thread, always 2 paired nucleotides


            if "X" in line:
                a = 0
                #b = 1
                l = []
                #z = line.count("Y")
                #print(z)
                #print(type(l))
                k = line[a] #+line[b]
                for i in range (4):
                    line=line.replace(" ", "")
                    line = line.replace("X", "")
                    line = line.replace("Y", "")
                    k=line[a] #+line[b]
                    l.append(k)
                    a=a+1
                    #b=b+2
                    #print(l)


                # Now we are adding 1 nucleotide in the middle of our basepair that we received from list l above. We are doing this 4 times, 1 time for each nucleotide
                # We are reversing our nucleotide pair sequence as well to get an 5' to 3' conformation
                #1
                YbaseA= []
                for i in l :
                    i=list(i)

                    i.insert(1,"A")
                    i.reverse()
                    i=str(i)
                    i.replace(",", "")
                    YbaseA.append(i)
                #print(YbaseA)

                #2
                YbaseC= []
                for i in l :
                    i=list(i)

                    i.insert(1,"C")
                    i.reverse()
                    i=str(i)
                    i.replace(",", "")
                    YbaseC.append(i)
                #print(YbaseC)


                #3
                YbaseG= []
                for i in l :
                    i=list(i)

                    i.insert(1,"G")
                    i.reverse()
                    i=str(i)
                    i.replace(",", "")
                    YbaseG.append(i)
                #print(YbaseG)


                #4
                YbaseU= []
                for i in l :
                    i=list(i)

                    i.insert(1,"U")
                    i.reverse()
                    i=str(i)
                    i.replace(",", "")
                    YbaseU.append(i)
                #print(YbaseU)

                #print("\n")




            else:
                a = 0
                #b = 1
                l = []
                #z = line.count("Y")
                #print(z)
                #print(type(l))
                k = line[a] #+line[b]
                for i in range (4):
                    line=line.replace(" ", "")
                    line = line.replace("X", "")
                    line = line.replace("Y", "")
                    k=line[a] #+line[b]
                    l.append(k)
                    a=a+1
                    #b=b+2
                    #print(l)


                # Now we are adding 1 nucleotide in the middle of our basepair that we received from list l above. We are doing this 4 times, 1 time for each nucleotide
                # We are reversing our nucleotide pair sequence as well to get an 5' to 3' conformation
                #1
                YbaseA= []
                for i in l :
                    i=list(i)

                    #i.insert(1,"A")
                    i.reverse()
                    i=str(i)
                    i.replace(",", "")
                    YbaseA.append(i)
                #print(YbaseA)

                #2
                YbaseC= []
                for i in l :
                    i=list(i)

                    #i.insert(1,"C")
                    i.reverse()
                    i=str(i)
                    i.replace(",", "")
                    YbaseC.append(i)
                #print(YbaseC)


                #3
                YbaseG= []
                for i in l :
                    i=list(i)

                    #i.insert(1,"G")
                    i.reverse()
                    i=str(i)
                    i.replace(",", "")
                    YbaseG.append(i)
                #print(YbaseG)


                #4
                YbaseU= []
                for i in l :
                    i=list(i)

                    #i.insert(1,"U")
                    i.reverse()
                    i=str(i)
                    i.replace(",", "")
                    YbaseU.append(i)
                #print(YbaseU)

                #print("\n")




            #--------------------------------------------------------------------------------------------------





            line = file.readline()


            for i in range(1):
                line=file.readline()


            #-----------------------------------------------------------------------------------------------------------------------
            #trying to start listin all our values in an dictionary
            #we need to connect two keys (thread1 and thread2) with one value





            allX = [XbaseA, XbaseC, XbaseG, XbaseU]
            allY = [YbaseA, YbaseC, YbaseG, YbaseU]
            #print(allX)


            m = 0

            baseY = allY[m]
            #print(baseY[m])

            for i in range(1):



                # i cut the \n away while line is a list the, split it by its " " and filter those away
                #now we have a nice clean list just with our values including all negative prefixes
                line = line.replace("\n", "")
                line=line.split(" ")
                line= list(filter(None, line))
                #print(line)


                # -----> our looping counters
                # allY should change its list every new line(4times x 6)
                # baseY should change its index after current element beeing applied to 4 values
                # allX should change its list for every element of the line, but go back to index 0 when it arrived at index 5
                # baseX index should raise up +1 every time the same list gets applied again(4times)
                # looping over every single element of our energy parameter list (line)

                countline = 0
                g = 0
                p = 0
                q = 0

                #print(XbaseA)
                baseX = allX[m]
                #print(allY[m])


                #print(baseY)

                #print(line)
                #print(allValues)
                #print("\n")
                #allValues={}
                for i in line:
                    if i == '.':

                        line[g] = 0

                        baseXX = baseX[q]
                        baseY = allY[p]
                        baseYY = baseY[q]

                        #--------converted them to float and str, dont know if thats necessary
                        line[g] = float(line[g])
                        baseXX = str(baseXX)
                        baseYY = str(baseYY)
                        #-------------------------------------------
                        #print(baseXX)
                        print(baseXX, baseYY, line[g])

                        #allValues[l[g]]=line[h]+line[j]+line[k]
                        allValues[baseXX, baseYY]=line[g]
                        #print(allValues)
                        g=g+1
                        p=p+1
                        if p == 4:
                            q = q+1
                            p = 0
                    else:

                        baseXX = baseX[q]
                        baseY = allY[p]
                        baseYY = baseY[q]

                        #--------converted them to float and str, dont know if thats necessary
                        line[g] = float(line[g])
                        baseXX = str(baseXX)
                        baseYY = str(baseYY)
                        #-------------------------------------------
                        #print(baseXX)
                        print(baseXX, baseYY, line[g])

                        #allValues[l[g]]=line[h]+line[j]+line[k]
                        allValues[baseXX, baseYY]=line[g]
                        #print(allValues)
                        g=g+1
                        p=p+1
                        if p == 4:
                            q = q+1
                            p = 0
                #print(allValues)
                #print("\n")
                m = m+1





                line= file.readline()

        #-------------------------------------------------------------------------------------------------------------------------


        #line = line.replace("\t", "")
        #line = line.replace("\n", "")
        #line = line.replace(" ", "")
        #D[line[0:6]]= line[6:10]


        else:
            line=file.readline()
        #print(allValues)

    file.close()

    os.chdir("/usr/local/lib/python3.5/dist-packages/numpy/lib")

    numpy.save('dangledict', allValues)
    dangle = numpy.load('dangledict.npy').item()
    #for key in allValues:
    #print(key)
    #print(stack.keys)
    value = dangle.values()
    #print(value)
    #for i in value:
    #print(type(i))

    #print(allValues.get('TGT'))

    #print(allValues["['A', 'U', 'A']", "['T', 'U', 'T']"])

    #allValues(['C', 'G', 'G'] ['C', 'A', 'G'])
    #print(allValues.keys())
    #print(allValues)
    #print(allValues["CGC", "GGG"])

#return(allValues)
dangleend()
import numpy
#stack = numpy.load('stackdict').item()
#print(stack)
dangle = numpy.load('dangledict.npy').item()
#print(dangle["['A', 'A']", "['U', 'U']"])
#print(dangle)
