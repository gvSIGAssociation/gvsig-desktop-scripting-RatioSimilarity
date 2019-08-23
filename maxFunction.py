# encoding: utf-8

import gvsig

from org.apache.commons.lang3 import Range
from java.lang import Integer
from org.gvsig.expressionevaluator.spi import AbstractFunction
from org.gvsig.expressionevaluator import ExpressionRuntimeException
from org.gvsig.expressionevaluator import MutableSymbolTable
from org.gvsig.expressionevaluator import ExpressionEvaluatorLocator
import sys

class MaxFunction(AbstractFunction):
    NAME = "MAX"

    def __init__(self):
      AbstractFunction.__init__(self, "Numeric", 
                self.NAME, 
                Range.between(Integer(3),Integer(4)),
                "The max() function evaluate for every element of the iterable and return the one with max value"+
                "If the second expression it's not set, it will return the value from the first expression",
                self.NAME+"( iterable, varname, expression, expression )",
                ["iterable - iterable object where the expression will be applied",
                 "varname - name that will have the iterable element in the expression",
                 "expression - expression to calculate the value to compare in the max function",
                 "expression - (optional) expression to calculate the value from that element to return"],
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
        maxValue = None
        maxReference = None
        exp = ExpressionEvaluatorLocator.getExpressionEvaluatorManager().createExpression()
        for element in iterable:
          symbolTable.setVar(varname, element)
          exp.setPhrase(exp1)
          value = exp.execute(symbolTable)
          if value > maxValue or maxValue==None:
            maxValue = value
            maxReference = element.getReference()
        if exp2==None:
          exp2 = exp1
        if maxReference!=None:
          symbolTable.setVar(varname, maxReference.getFeature())
          exp.setPhrase(exp2)
          resultValue = exp.execute(symbolTable)
        return resultValue

    
def main(*args):

    import eFactory
    eFactory.main()
