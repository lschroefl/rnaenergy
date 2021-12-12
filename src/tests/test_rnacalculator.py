'''
Tests for my rnacalculator.py module

arrange
act
assert

'''


# import rnaenergy.rnacalculator
from rnaenergy import rnacalculator
import os
import pytest

def test_one(monkeypatch):

    dirname = os.path.dirname(__file__)
    dir_rnasequence = os.path.join(dirname, '../../example/example3.txt')
    monkeypatch.setattr('builtins.input', lambda _: dir_rnasequence)

    result = rnacalculator.calculate()
    assert result == -20.104261104971467

    #fileorig = input ("Please enter the name of the text file annotation the RNA molecule. \n Specifiy the path to the file as well (if it is not contained within the current working directory).")
    #assert fileorig == dir_rnasequence

def test_inputformat(monkeypatch):
    dirname = os.path.dirname(__file__)
    dir_rnasequence = os.path.join(dirname, '../../example/example3.webp')
    monkeypatch.setattr('builtins.input', lambda _: dir_rnasequence)

    with pytest.raises(rnacalculator.InputError):
        result = rnacalculator.calculate()
