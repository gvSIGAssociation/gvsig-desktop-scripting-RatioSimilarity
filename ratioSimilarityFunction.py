# encoding: utf-8

import gvsig
from org.gvsig.expressionevaluator.spi import AbstractFunction
from org.apache.commons.lang3 import Range
from java.lang import Integer
from org.apache.commons.lang3 import StringUtils
import sys
#from org.apache.commons.text.similarity import JaroWinklerDistance

class RatioSimilarityFunction(AbstractFunction):
    NAME = "RATIOSIM"
    def __init__(self):
      AbstractFunction.__init__(self, "Numeric", 
                self.NAME, 
                Range.is(Integer(2)),
                "The RATIOSIM() function calculates the similarity between two numbers (min number/max number) o between strings (using JaroWinklerDistance) ",
                self.NAME+"( valueA, valueB )",
                ["valueA - numeric or string value", "valueB - numeric or string value"],
                "Object",
                False
        )
    def allowConstantFolding(self):
        return True

    def call(self, interpreter, args):
        a = self.getObject(args, 0)
        b = self.getObject(args, 1)
        if (isinstance(a, int) or isinstance(b, float)) and (isinstance(b, int) or isinstance(b, float)):
            n = min(a, b)
            m = max(a, b)
            ratio = (float(n)/m) 
            return ratio
        elif isinstance(a, basestring) and isinstance(b, basestring):
          jaroDistance = StringUtils.getJaroWinklerDistance(a, b)
          return jaroDistance
        else:
          return None

def main(*args):
    r = RatioSimilarityFunction()
    import eFactory
    eFactory.main()