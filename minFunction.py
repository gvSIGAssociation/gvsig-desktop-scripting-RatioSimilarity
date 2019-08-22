# encoding: utf-8

import gvsig

from org.apache.commons.lang3 import Range
from java.lang import Integer
from org.gvsig.expressionevaluator.spi import AbstractFunction
from org.gvsig.expressionevaluator import ExpressionRuntimeException
from org.gvsig.expressionevaluator import MutableSymbolTable
from org.gvsig.expressionevaluator import ExpressionEvaluatorLocator
import sys

class MinFunction(AbstractFunction):
    NAME = "MIN"

    def __init__(self):
      AbstractFunction.__init__(self, "Numeric", 
                self.NAME, 
                Range.between(Integer(3),Integer(4)),
                "The min() function evaluate body for every element of the iterable and return the one with max value",
                self.NAME+"( iterable, varname, expression, expression )",
                None,
                "Object",
                False
        );

    def useArgumentsInsteadObjects(self):
        return True
        
    def allowConstantFolding(self):
        return False
    
    #def call(Interpreter interpreter, args) throws Exception {
    #    throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    #}
    
    def call(self, interpreter, args):
        if not isinstance(interpreter.getSymbolTable(),  MutableSymbolTable):
            raise ExpressionRuntimeException("The use of forech loops require a mutable symbol table.")
        
        symbolTable = interpreter.getSymbolTable() #MutableSymbolTable
        
        body = None
        iterable = self.getObject(interpreter, args, 0) #Iterableprint varname
        varname = self.getObject(interpreter, args, 1)#.toString()
        exp1 = self.getObject(interpreter, args, 2)
        exp2 = None
        if args.size()==4:
          exp2 = self.getObject(interpreter, args, 3)
        minValue = None
        minReference = None
        exp = ExpressionEvaluatorLocator.getExpressionEvaluatorManager().createExpression()
        for element in iterable:
          symbolTable.setVar(varname, element)
          exp.setPhrase(exp1)
          value = exp.execute(symbolTable)
          if value < minValue or minValue==None:
            minValue = value
            minReference = element.getReference()
        if exp2==None:
          exp2 = exp1
        if minReference!=None:
          symbolTable.setVar(varname, minReference.getFeature())
          exp.setPhrase(exp2)
          resultValue = exp.execute(symbolTable)
        return resultValue

    
def main(*args):

    import eFactory
    eFactory.main()
