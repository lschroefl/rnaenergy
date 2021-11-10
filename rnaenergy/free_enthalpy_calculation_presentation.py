# just calculating the free enthalpy energy of known structure conformations

import math
import os
import numpy
import __future__
import forgi




import forgi.utilities.stuff as fus


def calculator():

    file = input("Please enter the name of the text file which contains you RNA sequence of interest. \n Please make sure your sequence starts with 'Seq: ' and your dot-bracket notation with 'Str: '. \n" ) 
    direction = input("Please put in the directory which contains the file. \n")
    
    os.chdir(direction)
    file=open(file)

    os.chdir("/usr/local/lib/python3.5/dist-packages/numpy/lib")
    
    stackdict = numpy.load('stackdict.npy').item()
    terminaldict = numpy.load('terminaldict.npy').item()
    wholelength = numpy.load('loopdict.npy').item()
    int1x1 = numpy.load('int11dict.npy').item()

    T = 310.15 # Kelvin, absolute temperature of the folding
    R = 1.987 # cal/mol*degree, gas konstante
    intermolec_initation = 4.09 #kcal/mol
    asymmetrie = 0.6 #kcal/mol


    hairpin = {}
    internal = {}
    bulge = {}
    
    
    for element in wholelength:
        if element[1] == 'Hairpin':
            hairpin[element]= wholelength[element]

    for element in wholelength:
        if element[1] == 'Internal':
            internal[element]= wholelength[element]

    for element in wholelength:
        if element[1] == 'Bulge':
            bulge[element]= wholelength[element]
            
    
    line = file.readline()

    enthalpybulge = 0
    enthalpyinternal = 0
    enthalpystack= 0
    enthalpyhairpin = 0

    printcontrol = 0

   
        
    while line != "":

#----------------------------Starting oat our sequence of interest, reading it, saving it as "sequence"-----------------------------------------------------------------------------------------------------------       
        if "Seq" in line :
            line = line.replace("Seq: ", "")
            line = line.replace ("t", "T")
            line = line.replace ("T", "U")
            sequence = line.replace("\n", "")
            totalrnaleng = len(sequence)
            line = file.readline()



#---------------------------Going to the next line, checking if "Str" in line, saving it as structure-----------------------------------------------------------------------------
            if "Str" in line:


#------------------------------controls the output to the shell, so that print the free enthalpy value only once for each sequence (in case file contains more than one RNA strand of interest----------------------------------------
                if enthalpystack != printcontrol:
                    free_enthalpy = enthalpybulge + enthalpyinternal + enthalpyhairpin + enthalpystack
                    print(" \n The total Gibbs free energy of this RNA strand is ", free_enthalpy, " kcal/mol in total. \n")
                    printcontrol = enthalpystack
                else:
                    printcontrol = enthalpystack
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                enthalpybulge = 0
                enthalpyinternal = 0
                enthalpystack= 0
                enthalpyhairpin = 0
                
                structure = line.replace("Str: ", "")
                structure = structure.replace(" ", "")
                structure = structure.replace("\n", "")
                structure = structure.replace("<", ")")
                structure = structure.replace(">", "(")

                
                
#----------- applying the forgi.utilities.stuff module on our dot-bracket notation, OUTPUT = pairtable (list where each element shows the index of the base-pairing partner, if not paired value=0)-----------
                pairtablelong = fus.dotbracket_to_pairtable(structure)
                pairtable = pairtablelong[1:]
 
                counter = 0
               
                for element in pairtable:
                    
#----------------------------if element = 0 -> nucleotide is not paired, calculation of all kind of loops (hairpin, internal, bulge)------------------------------                    
                    if element == 0:
                        

                        forwardcounter = counter 
                        backwardcounter = counter -1
                        
                        if forwardcounter >= totalrnaleng:
                            break
                        else:
                            forwardneighbor = pairtable[forwardcounter]


#--------------------two infinite loops, searching in the front and in the back of our element the nex element that is not 0, if found its assigned to forwardneighbor and backwardneighbor --------------------------------------

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


                                
#------------------------------Hairpin loop----------------------------------------------------------------------------------------------------------------------------------------------------------
                        #backwardcounter and forwardcounter are index numbers, arrive from our counter#
                        # index 0 in our pairtable is len(structure)#
                        # backwardneighbor and forwardneighbor are the values which appear at the specific index(backwardcounter or forwardcounter), so they are 1 greater than the index numbers#
                        
                            if backwardcounter+1 == forwardneighbor :
                                
                                loopsize = forwardcounter-(backwardcounter+1)        
                                pair = sequence[backwardcounter]+sequence[backwardcounter+1],sequence[forwardcounter-1] + sequence[forwardcounter]

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
                                        print(counter, sequence[counter], " -> hairpinloop ")#, enthalpyhairpin)
                                       



#---------------------------------------interior loops and bulge loops -----------------------------------------------------------------------------------------------------------------------------------------------
                                #defining loopornoloop with whom we check if we have unpaired bases at the interacting, opposite strand#
                                # defining unpaired_bases total#
                                
                        
                            else:
                                misslength = forwardcounter - (backwardcounter +1)   # plus one because its the index of our list, starts with 0 not 1#
                                loopornoloop = backwardneighbor - forwardneighbor   # not plus 1 because its the value of the pairtable, starts with 1#
                                unpaired_bases_total = misslength + loopornoloop
                                unpaired_bases_total = float(unpaired_bases_total)
                                    
#-------------------------------------now we check if we have unpaired bases at the interacting part of the strain as well-----------------------
                                #if yes we have an internal loop# 
                                
                                if loopornoloop > 1:
                                    
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
                                                print(counter, sequence[counter], " -> internal loop 1x1 -> ")#, enthalpyinternal)
                                            
                                               
                                    elif unpaired_bases_total <= 6:
                                      
                                        
                                        enthalpyinternal = enthalpyinternal + (intermolec_initation + internal[(unpaired_bases_total, "Internal")] + asymmetrie*(misslength-loopornoloop) ) / unpaired_bases_total

                                        print(counter, sequence[counter], " -> internal loop -> ")#, enthalpyinternal)
                                        
                                    elif unpaired_bases_total > 6:

                                        initation = internal[(6,"Internal")]+1.08*math.log(unpaired_bases_total/6)
                                        enthalpyinternal = enthalpyinternal + (intermolec_initation + initation + asymmetrie*(misslength-loopornoloop) ) / unpaired_bases_total


                                        print(counter, sequence[counter], " -> internal loop conatins in total of ", unpaired_bases_total, " unpaired nucleotides. ")#, enthalpyinternal)
                                        print("Could be a pseudoknot or multiloop as well, this programm is not able to differentiate those. ")


#------------------------------------bulge loop: we have no unpaired nucleotides at the opposite strand---------------------------------------------------
                                                                            
                                else:
                                    
                                    if 1 < misslength <= 6:
                                        enthalpybulge = enthalpybulge + (bulge[(misslength, "Bulge")])/misslength
                                        print(counter, sequence[counter], " -> bulge -> ")#, enthalpybulge)
                                    if misslength > 6:
                                        enthalpybulge = enthalpybulge + (bulge[('6', 'Bulge')] + 1.75*R*T*math.log(misslength/6))/misslength
                                            
                                    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                            
                            
                        


                        
                        counter = counter + 1
 #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                      
                    else:


                        endindex = element-1
                        startindex = pairtable[endindex] -1
                        

#------------------------------------------Stack pairs------------------------------------------------------------------------------------------------------------
                        #calculating the energy values for our stack pairs, but twice the amount because we go over every pair 2 times#
                         

                        if startindex+1 < len(pairtable):
                            

                            if pairtable[startindex +1] != 0:
                                partnerstart = startindex +1
                                partnerend = endindex- 1


                            # when the middle of the strand is i change the start-string to the end-string and contrary the same# 

                                if startindex > endindex:
                                    pair = sequence[partnerend]+sequence[endindex], sequence[startindex]+sequence[partnerstart]
                                else:
                                    pair = sequence[startindex]+sequence[partnerstart],sequence[partnerend] + sequence[endindex]
                            

                                for bothkey in stackdict:

                    #changing the dictionary keys into tulples, with exactly the same structure as pair#
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
                                        enthalpystack = enthalpystack+(stackdict[bothkey]/2)
                                        print (counter, sequence[counter], " -> stack ->"),#enthalpystack) 
                                        

                                
                        counter = counter +1  
                
                line = file.readline()
#--------------------------------------------------------exiting our loop -----------------------------------------------------------------------------------               
        else:
            line = file.readline()

#--------------------------again the printcontrol--------------------------------------------------------------------------------------------------------------------------       
        
        if enthalpystack != printcontrol:
            free_enthalpy = enthalpybulge + enthalpyinternal + enthalpyhairpin + enthalpystack
            print(" \n The total difference of Gibbs free energy of this RNA strand compared to a completely unpeired strand is ", free_enthalpy, " kcal/mol in total. \n")
            printcontrol = enthalpystack
        else:
            printcontrol = enthalpystack

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------         

calculator()
            
           
