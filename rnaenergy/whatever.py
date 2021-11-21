from importlib import resources  #used to read resources included in the package
import io
import importlib

#import pkgutil
#file = pkgutil.get_data(__name__, "energytable/dangle.txt").decode()
#print(file)

import importlib_resources
my_resources = importlib_resources.files("rnaenergy") / "energytable"
file = (my_resources / "dangle.txt").read_text()
#print(text)
with open("dangle.txt" , 'w') as f:
    f.writelines(file)
