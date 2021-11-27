import math
import numpy
import forgi.utilities.stuff as fus
import os

def calculate():

    """
    weak points
    1. my npy files are just saved to the working directory from which the script is called
    1. I then manually transfered them to rnaenergy/energytable. Perfect would be a creating and storing as

    2. I will now try to use the naiv approach with os.path.join to load my .npy files via numpy load..
    2. I wanted to not use this approach as it seems to create problems when the package is loaded from a zip file, but for now its a quick fix

    todo at some point
    the functions for the creation of the .npy dicts should be called directly from rnacalulator, the .npy files stored in this process
    in the package energytable, and from there accessed by rnacalculator.calculator without using os.path

    """


    fileorig = input ("Please enter the name of the text file annotation the RNA molecule. \n Specifiy the path to the file as well (if it is not contained within the current working directory).")
    file=open(fileorig)

    print(os.getcwd())
    dirname = os.path.dirname(__file__)

    # loading my .npy dicts that were previously created
    terminaldict = numpy.load(os.path.join(dirname, 'energytable/terminaldict.npy'), allow_pickle=True).item()
    wholelength = numpy.load(os.path.join(dirname, 'energytable/loopdict.npy'), allow_pickle=True).item()
    int1x1 = numpy.load(os.path.join(dirname, 'energytable/int11dict.npy'), allow_pickle=True).item()
    stackdict = numpy.load(os.path.join(dirname, 'energytable/stackdict.npy'), allow_pickle=True).item()


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
        if "Seq" in line :
            line = line.replace("Seq: ", "")
            line = line.replace ("t", "T")
            line = line.replace ("T", "U")
            sequence = line.replace("\n", "")
            totalrnaleng = len(sequence)

        
            #reading out our dot bracket notation
            line = file.readline()
            if "Str" in line:

                if enthalpystack != printcontrol:
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
                
                pairtablelong = fus.dotbracket_to_pairtable(structure)
                pairtable = pairtablelong[1:]

                counter = 0
               
                
                for element in pairtable:
                    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                    
                    if element == 0:

                        forwardcounter = counter 
                        backwardcounter = counter -1

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
                            #backwardneighbor und forwardneighbor correspond to position in pairtable (index+1)


                            if forwardneighbor != 0 :
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                            #Hairpin loop
                            #backwardcounter and forwardcounter correspond to index, start at 0
                            #backwardneighbor und forwardneighbor correspond to the pairtable (index +1)
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
                                            print(counter, sequence[counter], " -> hairpinloop ", enthalpyhairpin)



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                            #bulge and interior loops 
                                else:
                                    misslength = forwardcounter - (backwardcounter +1)   # plus one because its the index of our list, starts with 0 not 1
                                    loopornoloop = backwardneighbor - forwardneighbor   # not plus 1 because its the value of the pairtable, starts with 1
                                    unpaired_bases_total = misslength + loopornoloop
                                    unpaired_bases_total = float(unpaired_bases_total)
                                        

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
                                                    print(counter, sequence[counter], " -> internal loop 1x1 -> ", enthalpyinternal)

                                        elif unpaired_bases_total <= 6:

                                            enthalpyinternal = enthalpyinternal + (intermolec_initation + internal[(unpaired_bases_total, "Internal")] + asymmetrie*(misslength-loopornoloop) ) / unpaired_bases_total
                                            print(counter, sequence[counter], " -> internal loop -> ", enthalpyinternal)
                                            
                                        elif unpaired_bases_total > 6:

                                            initation = internal[(6,"Internal")]+1.08*math.log(unpaired_bases_total/6)
                                            enthalpyinternal = enthalpyinternal + (intermolec_initation + initation + asymmetrie*(misslength-loopornoloop) ) / unpaired_bases_total


                                            print(counter, sequence[counter], " -> internal loop conatins ", unpaired_bases_total, " unpaired nucleotides. ", enthalpyinternal)
                                            print("\n Alternatively a pseudoknot or a multiloop could be present, as these structures are not recognized by the algorithm. ")
                                            
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


                    # index of strings starts at 0, index of pairtable at 1, therefore subtraction by 1 necessary
                        endindex = element-1
                        startindex = pairtable[endindex] -1


#------------------------------------------------------------------------------------------------------------------------------------------------------
                        #calculating the energy values for our stack pairs, but twice the amount because we go over every pair 2 times, so we will divide by 2 in the end
                        # i change it a little bit we still have to 
                        if startindex+1 < len(pairtable):
                            

                            if pairtable[startindex +1] != 0:
                                partnerstart = startindex +1
                                partnerend = endindex- 1

                                if startindex > endindex:
                                    pair = sequence[partnerend]+sequence[endindex], sequence[startindex]+sequence[partnerstart]
                                else:
                                    pair = sequence[startindex]+sequence[partnerstart],sequence[partnerend] + sequence[endindex]

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

                                    if key == pair:
                                        enthalpystack = enthalpystack+(stackdict[bothkey]/2)
                                        print (counter, sequence[counter], " -> stack ->", enthalpystack) 


                        counter = counter +1

                
                line = file.readline()

        else:
            line = file.readline()


        if enthalpystack != printcontrol:
            free_enthalpy = enthalpybulge + enthalpyinternal + enthalpyhairpin + enthalpystack
            print(" \nThe amount of Gibbs Free Energy released through this secondary conformation adds up to ", free_enthalpy, " kcal/mol in total. \n")
            printcontrol = enthalpystack
        else:
            printcontrol = enthalpystack

           


            
           
