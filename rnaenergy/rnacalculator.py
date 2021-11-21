# just calculating the free enthalpy energy of known structure conformations

import math
import os
import re
import numpy
import __future__
#import scipy

os.getcwd()

import forgi

#import dotbracket_to_graph.py
#import forgi.graph
#import forgi.aux


import forgi.utilities.stuff as fus
#from forgi.graph import bulge_graph as fbg
#bg = forgi.BulgeGraph()


def calculator():

    fileorig = input("Please enter the name of the text file containing RNA-seq and dot-bracket annotation. \n Please make sure your sequence starts with 'Seq: ' and your dot-bracket notation with 'Str: '. \n" )
    direction = input("Please specifiy the path to the file \n")
    
    os.chdir(direction)
    file=open(fileorig)

    #os.chdir("/usr/local/lib/python3.5/dist-packages/numpy/lib")
    import rnaenergy
    import importlib_resources
    my_resources = importlib_resources.files("rnaenergy")
    file = (my_resources / "int11dict.npy")  # .read_text()
    #file = file.open()
    int1x1 = numpy.load(file, allow_pickle=True).item() ### FUCKING WORKS WHAT THE HELL
    print(int1x1)

    int11.stack()
    # todo learn how to call all my addtional functions at the beginning of the calculator to create my dicts
    # todo (in the end I want to be able to do everything with just calling the calulator
    stackdict = numpy.load('stackdict.npy').item()
    terminaldict = numpy.load('terminaldict.npy').item()
    wholelength = numpy.load('loopdict.npy').item()
    int1x1 = numpy.load('int11dict.npy').item()

    T = 310.15 # Kelvin, absolute temperature of the folding
    R = 1.987 # cal/mol*degree, gas konstante
    intermolec_initation = 4.09 #kcal/mol
    asymmetrie = 0.6 #kcal/mol

    #print(int1x1)
    #print(stackdict)
    #print(wholelength)
    hairpin = {}
    internal = {}
    bulge = {}
    #structure = ["(", ".", "(", ".", ")", ".","(",".", "(", ")", ")", ")"]
    #structure = input("put in the dot-bracket notation.")
    
    for element in wholelength:
        if element[1] == 'Hairpin':
            hairpin[element]= wholelength[element]

    for element in wholelength:
        if element[1] == 'Internal':
            internal[element]= wholelength[element]

    for element in wholelength:
        if element[1] == 'Bulge':
            bulge[element]= wholelength[element]
            
    #print(hairpin)
    #print(internal)
    #print(bulge)
    #print(missterm)
    
    line = file.readline()

    enthalpybulge = 0
    enthalpyinternal = 0
    enthalpystack= 0
    enthalpyhairpin = 0

    printcontrol = 0

   
                
    while line != "":
        if "Seq" in line :
            line = line.replace("Seq: ", "")
            line = line.replace ("t", "T")
            line = line.replace ("T", "U")
            sequence = line.replace("\n", "")
            #print(sequence)
            totalrnaleng = len(sequence)
            #print(n)

        
            #reading out our dot bracket notation
            line = file.readline()
            if "Str" in line:

                if enthalpystack != printcontrol:
                    #print(enthalpybulge)
                    #print(enthalpyinternal)
                    #print(enthalpyhairpin)
                    #print(enthalpystack)
                    free_enthalpy = enthalpybulge + enthalpyinternal + enthalpyhairpin + enthalpystack
                    print(" \n The total Gibbs free energy of this RNA strand is ", free_enthalpy, " kcal/mol in total. \n")

                    printcontrol = enthalpystack
                else:
                    printcontrol = enthalpystack

                enthalpybulge = 0
                enthalpyinternal = 0
                enthalpystack= 0
                enthalpyhairpin = 0
                
                structure = line.replace("Str: ", "")
                structure = structure.replace(" ", "")
                structure = structure.replace("\n", "")
                structure = structure.replace("<", ")")
                structure = structure.replace(">", "(")

                numberopen = structure.count("(", 0, len(structure))
                numberclosed = structure.count(")", 0, len(structure))
                #print(structure)
                
                pairtablelong = fus.dotbracket_to_pairtable(structure)
                #print(pairtable)
                #print(pairtable[0], structure[0])
                pairtable = pairtablelong[1:]

                #print(numberopen, numberclosed, len(structure), len(index))
                #print(index)
                #print(sequence,"\n", pairtable)

                #print(type(pairtable))

                #print(len(sequence), len(pairtable))

                counter = 0
               
                
                for element in pairtable:
                    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
                    if element == 0:


                        
                        

                        forwardcounter = counter 
                        backwardcounter = counter -1
                        #forwardneighbor = pairtable[forwardcounter]

                        if forwardcounter >= totalrnaleng:
                            break
                        else:
                            forwardneighbor = pairtable[forwardcounter]

                            while forwardneighbor == 0:

                                forwardcounter = forwardcounter +1
                                bulgecounter = forwardcounter - counter
                                if forwardcounter >= totalrnaleng:
                                    break
                                else:
                                    forwardneighbor = pairtable[forwardcounter]
                                
                            backwardneighbor = pairtable[backwardcounter]

                            while backwardneighbor == 0:
                                backwardcounter = backwardcounter -1
                                backwardneighbor = pairtable[backwardcounter]


                                
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                            #Hairpin loop
                            #backwardcounter and forwardcounter correspond to the index of the current position
                           # backwardneighbor und forwardneighbor correspond to position in pairtable (index+1)


                            if forwardneighbor != 0 :
                                #print (backwardcounter, backwardneighbor, forwardneighbor, forwardcounter, counter)



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                            #Hairpin loop
                            #backwardcounter und forwardcounter sind die richtigen index zahlen, kommen vom counter
                            # backwardneighbor und forwardneighbor sind die werte des pairtables also index +1
                                if backwardcounter+1 == forwardneighbor :
                                    
                                    #print ("hairpin loop")
                                    loopsize = forwardcounter-(backwardcounter+1)
                           
                            
                                    pair = sequence[backwardcounter]+sequence[backwardcounter+1],sequence[forwardcounter-1] + sequence[forwardcounter]
                                    #print(pair)
                                       #print(type(pair))

                                    for bothkey in terminaldict:
                                        startkey = bothkey[0]
                                        endkey = bothkey[1]

                                        endkey = endkey.replace(",", "")
                                        endkey = endkey.replace("'", "")
                                        endkey = endkey.replace("[", "")
                                        endkey = endkey.replace("]", "")
                                        endkey = endkey.replace(" ", "")
                                        startkey = startkey.replace(",", "")
                                        startkey = startkey.replace("'", "")
                                        startkey = startkey.replace("[", "")
                                        startkey = startkey.replace("]", "")
                                        startkey= startkey.replace(" ", "")

                                        key = startkey, endkey

                                        if key == pair:
                                            enthalpyhairpin = enthalpyhairpin+(terminaldict[bothkey]/loopsize) + hairpin[(loopsize, "Hairpin")]/loopsize
                                            print(counter, sequence[counter], " -> hairpinloop ", enthalpyhairpin)
                                            #print("hairpin loop", loopsize, key, startindex, endindex)



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                            #bulge and interior loops 
                                else:
                                    misslength = forwardcounter - (backwardcounter +1)   # plus one because its the index of our list, starts with 0 not 1
                                    loopornoloop = backwardneighbor - forwardneighbor   # not plus 1 because its the value of the pairtable, starts with 1
                                    unpaired_bases_total = misslength + loopornoloop
                                    unpaired_bases_total = float(unpaired_bases_total)
                                        

                                    if loopornoloop > 1:
                                        #print(len(sequence), len(pairtable))
                                        #print ("backward edge: ", backwardcounter, backwardneighbor, sequence[backwardcounter], sequence[backwardneighbor],
                                        #       "Position hole: ", sequence[counter], counter,"forward edge: ", forwardcounter, forwardneighbor, sequence[forwardcounter], sequence[forwardneighbor])
                                        if loopornoloop == 2 and misslength == 2:

                                            for bothkey in int1x1:

                                                startkey = bothkey[0]
                                                endkey = bothkey[1]

                                                endkey = endkey.replace(",", "")
                                                endkey = endkey.replace("'", "")
                                                endkey = endkey.replace("[", "")
                                                endkey = endkey.replace("]", "")
                                                endkey = endkey.replace(" ", "")
                                                startkey = startkey.replace(",", "")
                                                startkey = startkey.replace("'", "")
                                                startkey = startkey.replace("[", "")
                                                startkey = startkey.replace("]", "")
                                                startkey= startkey.replace(" ", "")

                                                key = startkey, endkey
                                                loop1x1 = sequence[backwardcounter]+sequence[counter]+sequence[forwardcounter], sequence[forwardneighbor] + sequence[backwardneighbor-1] + sequence[backwardneighbor]

                                                if key == loop1x1:
                                                    
                                                    enthalpyinternal = enthakpyintern + (int1x1[bothkey]/2)
                                                    print(counter, sequence[counter], " -> internal loop 1x1 -> ", enthalpyinternal)
                                                
                                                    #print ("backward edge: ", backwardcounter, backwardneighbor, sequence[backwardcounter], sequence[backwardneighbor],
                                                        #"Position hole: ", sequence[counter], counter,"forward edge: ", forwardcounter, forwardneighbor, sequence[forwardcounter], sequence[forwardneighbor])
                                        elif unpaired_bases_total <= 6:
                                            #print(loopornoloop, misslength)
                                            #print ("backward edge: ", backwardcounter, backwardneighbor, sequence[backwardcounter], sequence[backwardneighbor],
                                            #  "Position hole: ", sequence[counter], counter,"forward edge: ", forwardcounter, forwardneighbor, sequence[forwardcounter], sequence[forwardneighbor])
                                            
                                            enthalpyinternal = enthalpyinternal + (intermolec_initation + internal[(unpaired_bases_total, "Internal")] + asymmetrie*(misslength-loopornoloop) ) / unpaired_bases_total

                                            print(counter, sequence[counter], " -> internal loop -> ", enthalpyinternal)
                                            
                                        elif unpaired_bases_total > 6:

                                            initation = internal[(6,"Internal")]+1.08*math.log(unpaired_bases_total/6)
                                            enthalpyinternal = enthalpyinternal + (intermolec_initation + initation + asymmetrie*(misslength-loopornoloop) ) / unpaired_bases_total


                                            print(counter, sequence[counter], " -> internal loop conatins in total of ", unpaired_bases_total, " unpaired nucleotides. ", enthalpyinternal)
                                            print("Could be a pseudoknot or multiloop as well, this programm is not able to differentiate those. ")
                                            
                                    else:
                                        
                                        if 1 < misslength <= 6:
                                            enthalpybulge = enthalpybulge + (bulge[(misslength, "Bulge")])/misslength
                                            print(counter, sequence[counter], " -> bulge -> ", enthalpybulge)
                                        if misslength > 6:
                                            enthalpybulge = enthalpybulge + (bulge[('6', 'Bulge')] + 1.75*R*T*math.log(misslength/6))/misslength
                                            
                                    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                            
                            
                        


                        
                        counter = counter + 1
 #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                      
                    else:


                    # da der index eines str leider bei 0 startet muss ich die von den werten des pairtables 1 abziehen
                    # extrem verwirrend auf dauer
                        endindex = element-1
                        startindex = pairtable[endindex] -1
                        #print(startindex)
                        #print(sequence[startindex], sequence[endindex], startindex, endindex)

#------------------------------------------------------------------------------------------------------------------------------------------------------
                        #calculating the energy values for our stack pairs, but twice the amount because we go over every pair 2 times, i think thats wrong i have to change that shit
                        # i change it a little bit we still have to 
                        if startindex+1 < len(pairtable):
                            

                            if pairtable[startindex +1] != 0:
                                partnerstart = startindex +1
                                partnerend = endindex- 1

                                if startindex > endindex:
                                    pair = sequence[partnerend]+sequence[endindex], sequence[startindex]+sequence[partnerstart]
                                else:
                                    pair = sequence[startindex]+sequence[partnerstart],sequence[partnerend] + sequence[endindex]
                                #print(pair)
                                #print(type(pair))

                                for bothkey in stackdict:

                    #changing the dictionary keys into tulples, with exactly the same structure as pair
                                    startkey = bothkey[0]
                                    endkey = bothkey[1]

                                    endkey = endkey.replace(",", "")
                                    endkey = endkey.replace("'", "")
                                    endkey = endkey.replace("[", "")
                                    endkey = endkey.replace("]", "")
                                    endkey = endkey.replace(" ", "")
                                    startkey = startkey.replace(",", "")
                                    startkey = startkey.replace("'", "")
                                    startkey = startkey.replace("[", "")
                                    startkey = startkey.replace("]", "")
                                    startkey= startkey.replace(" ", "")

                                    key = startkey, endkey
                                    #print(key)
                                    
                                    #match = re.match(key, pair, re.I)
                                    #if match != None:
                                        #enthalpy = enthalpy + stackdickt[key]

                                    if key == pair:
                                        enthalpystack = enthalpystack+(stackdict[bothkey]/2)
                                        print (counter, sequence[counter], " -> stack ->", enthalpystack) 
                                        #print(key, startindex, partnerend)
                                        #print(enthalpy)
                            #print(key, startindex, partnerend)
                                    




                                
                        counter = counter +1
                #print(enthalpystack)
                #print(enthalpyhairpin)
                                  

            
                
                line = file.readline()
            
            #numpy.save("free_enthaply_of"+ fileorig, [sequence, structure, free_enthalpy])             
        else:
            line = file.readline()

        #enthalpystack muss ich noch in die hälfte teilen, enthalyhairpin ist bereits korrekt
        #if (enthalpybulge and enthalpyinternal and enthalpystack and enthalpyhairpin) != 0:
       
        #numpy.save("free_enthaply_of"+ fileorig, [sequence, structure, free_enthalpy]) 
        if enthalpystack != printcontrol:
            #print(enthalpybulge)
            #print(enthalpyinternal)
            #print(enthalpyhairpin)
            #print(enthalpystack)
            free_enthalpy = enthalpybulge + enthalpyinternal + enthalpyhairpin + enthalpystack
            print(" \n The total Gibbs free energy of this RNA strand is ", free_enthalpy, " kcal/mol in total. \n")
            printcontrol = enthalpystack
        else:
            printcontrol = enthalpystack

           

calculator()
            
           
