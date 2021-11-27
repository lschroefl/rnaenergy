# rnaenergy

The algorithm in this repository calculates free energy changes for RNA molecules with known secondary structure.
Free energy change quantifies the stability of a secondary RNA structure as compared to a completely unpaired RNA strand. 

How to get started: 
1. Install rnaenergy from pypi(*add the code to pull from repository*)
# dependencies should be installed automatically
2. Install dependencies (*add pip command to install from dependencies.txt)
3. from rnaenergy import rnacalculator
4. rnacalculator.calculate()
5. The program will ask for input
    - The input must be a single text file (.txt), speficying the nucleobase sequence and the secondary structure <br>
    in form of a dot-bracket annotation. See in the folder rnaenergy/example/ for examples (*add a picture with an example below)
    - specify the path to and the name of the text file (e.g. home/Desktop/example1.txt

Output: 
1. A list that specifies the secondary structure, and the thereby resulting free energy change (*kcal/mol*) for every position of your RNA sequence. 
2. The total free energy change (*kcal/mol*) of this secondary structure compared to the completely unpaired strand. 



Rational

In RNA the predominant amount of free enthalpy is released by the formation of secondary rather than tertiary structure.
The secondary structure of ribonucleic acids is usually stable context independent as isolated sequences. 
Furthermore, experimental and theoretical evidence indicates that secondary structure superiority in RNA extends beyond the thermodynamic domain and is influencing the chronology of folding as well, as it has been shown that
secondary structure forms first and thereafter guides the formation of tertiary RNA structure. 
*Vieregg JR 2010. Nucleic Acid Structural Energetics. In Encyclopedia of Analytical Chemistry (eds Meyers RA, Meyers RA). https://doi.org/10.1002/9780470027318.a1418.pub2*

![rna secondary structure](/images/rna.png)


This algorithm recognizes 4 different secondary motifs: bulge loops,
interior loops, hairpin loops and stacking regions. Pseudoknots, multiloops and dangling
ends are not recognized and therefore not calculated. I used parameters as well as
energy calculation formulas from the Nearest Neighbor
Database (https://rna.urmc.rochester.edu/NNDB/).
My programm is much simpler and not as exact as other packages calculating Gibbs free
energy values and secondary structures for RNA molecules (by example: The Vienna
RNA package). It ignores a lot of special base pairing (like GU closure or CG mismatch)
which other libraries and calculation don‘t, and ignores in general all exceptions and
special energy values. This algorithm is designed to get an average feeling for the free energy change, and not for any exact calculation

All free energy parameters used here were established by the Mathews's lab through optical melting studies. <br>
*Turner DH, Mathews DH. NNDB: the nearest neighbor parameter database for predicting stability of nucleic acid secondary structure. Nucleic Acids Res. 2010;38(Database issue):D280-D282. doi:10.1093/nar/gkp892*
<p>For more information please visit the website [Nearest Neighbor Database](http://rna.urmc.rochester.edu/NNDB). </p>



This code was written long time ago by me in course of my bachelor's thesis. <br>Many years passed already since then, but I thought I put it onto github rather than letting it dwell in oblivion on my old PC. 
