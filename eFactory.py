# encoding: utf-8

import gvsig

from org.gvsig.expressionevaluator.spi import AbstractSymbolTableFactory
from org.gvsig.expressionevaluator.spi import AbstractSymbolTable
from org.gvsig.expressionevaluator import ExpressionEvaluatorLocator

from addons.RatioSimilarity.minFunction import MinFunction
from addons.RatioSimilarity.maxFunction import MaxFunction
from addons.RatioSimilarity.ratioSimilarityFunction import RatioSimilarityFunction
from addons.RatioSimilarity.sumProductFunction import SumProductFunction

class RatioSimilaritySymbolTable(AbstractSymbolTable):
    NAME = "RatioSimilarity"
    
    def __init__(self):
        AbstractSymbolTable.__init__(self, self.NAME)
        self.addFunction(RatioSimilarityFunction())
        self.addFunction(MaxFunction())
        self.addFunction(MinFunction())
        self.addFunction(SumProductFunction())
        
class RatioSimilaritySymbolTableFactory(AbstractSymbolTableFactory):
    def __init__(self):
        AbstractSymbolTableFactory.__init__(self, RatioSimilaritySymbolTable.NAME, True)
        self.symbolTable = None

    def createSymbolTable(self, *args):
        if self.symbolTable==None:
            self.symbolTable = RatioSimilaritySymbolTable()
        
        return self.symbolTable
    

def main(*args):

    manager = ExpressionEvaluatorLocator.getManager();
    manager.registerSymbolTable(RatioSimilaritySymbolTableFactory());
