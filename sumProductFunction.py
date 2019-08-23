# encoding: utf-8

import gvsig
from org.gvsig.expressionevaluator.spi import AbstractFunction
from org.apache.commons.lang3 import Range
from java.lang import Integer

import sys

class SumProductFunction(AbstractFunction):
    NAME = "SUMPRODUCT"
    def __init__(self):
      AbstractFunction.__init__(self, "Numeric", 
                self.NAME, 
                Range.is(Integer(2)),
                "The SUMPRODUCT() function calculates the sumatory between two list of numbers.\n"+
                "Each value will be multiplied between its corresponding value in the other list before the sumatory",
                self.NAME+"( valueA, valueB )",
                ["listA - list of numeric values", "listB - list of numerics values"],
                "Double",
                False
        )
    def allowConstantFolding(self):
        return True

    def call(self, interpreter, args):
        values = self.getObject( args, 0)
        weight = self.getObject(args, 1)
        if values.size()!=weight.size():
          return None
        value = 0
        for v, w in zip(values, weight):
          currentValue = v * w
          value += currentValue
        return value
        

def main(*args):

    
    import eFactory
    eFactory.main()