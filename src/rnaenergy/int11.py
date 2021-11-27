def int():
    # todo comment according to guidelines
        import numpy
        import importlib_resources
        file = importlib_resources.open_text("energytable", "int11.txt", encoding = 'utf-8', errors='strict')


        D={}

        index = 0
    
        for i in range(20):
            i = file.readline()
        thumb = "A    C    G    U"
        thumb2 = "A    C    G    T"
        allValues={}
        
        line = file.readline()
        while line != "":
                
            #starting at our constant header "A  C  G  U"
            if thumb or thumb2 in line:
        
                #skipping unnecessary lines
                while "X" not in line:
                    line = file.readline()
                    line = line.replace(" ", "")
                    if line == "":
                        break
                    
                    
                if "X" in line:
                    z = line.count("X")
                    line = file.readline()
      
#----------------------------------------------------------------------------------------------5' 3'----------------
                #creating a list of our bases of interest, of ur 5' to 3' thread, always 2 paired nucleotides 
                    a = 0
                    b = 1
                    l = []
                    k = line[a] +line[b]    
                    for i in range (6):
                        line=line.replace(" ", "")
                        line = line.replace("X", "")
                        line = line.replace("Y", "")
                        k=line[a] +line[b]
                        l.append(k)
                        a=a+2
                        b=b+2
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

        
        #-----------------------------------------------------------------------------------------------3' 5'----------------------------
                #creating the second list of our bases of interest, of our 3' to 5' thread, always 2 paired nucleotides
        
                a = 0
                b = 1
                l = []
                z = line.count("Y")

                if line == "":
                    break
                for i in range (6):
                    line=line.replace(" ", "")
                    line = line.replace("X", "")
                    line = line.replace("Y", "")
                    k=line[a] +line[b]
                    l.append(k)
                    a=a+2
                    b=b+2
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
        
        #--------------------------------------------------------------------------------------------------
        
                    
        
        
        
                line = file.readline()
                                
                
                for i in range(2):
                    line=file.readline()
        
        
        #-----------------------------------------------------------------------------------------------------------------------
                    #trying to start listin all our values in an dictionary
                    #we need to connect two keys (thread1 and thread2) with one value
                    
        
                allX = [XbaseA, XbaseC, XbaseG, XbaseU]
                allY = [YbaseA, YbaseC, YbaseG, YbaseU]
                    
                m = 0
               
                baseY = allY[m]
                    
                for i in range(4):
        
                
                        
                    # i cut the \n away while line is a list the, split it by its " " and filter those away
                    #now we have a nice clean list just with our values including all negative prefixes
                    line = line.replace("\n", "")
                    line=line.split(" ")
                    line= list(filter(None, line))
        
        
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

                    baseX = allX[m]

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
                            allValues[baseXX, baseYY]=line[g]
                            g=g+1
                            p=p+1
                            if p == 4:
                                q = q+1
                                p = 0
                    #print(allValues)
                    m = m+1


                        
                            
                      
                    line= file.readline()
        
        #-------------------------------------------------------------------------------------------------------------------------

            else:
                line=file.readline()
            print(allValues)
                   
        file.close()
                

        numpy.save('int11dict', allValues, allow_pickle=True)
        int11 = numpy.load('int11dict.npy', allow_pickle=True).item()

int()
import numpy
dict = numpy.load('int11dict.npy', allow_pickle=True).item()
print(dict)
