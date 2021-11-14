from importlib import resources  #used to read resources included in the package
import io
import importlib

files = [
    "dangle.txt",
    "loop.txt",
    "stack.txt",
    "int11.txt",
    "stack.txt",
]

with resources.open_binary("RNA-gibbs-free-energy-calculator","dangle.txt" ) as ok:
    file = ok.read()


