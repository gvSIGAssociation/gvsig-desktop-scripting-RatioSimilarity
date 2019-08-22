# encoding: utf-8

import gvsig
from org.gvsig.expressionevaluator import ExpressionEvaluatorLocator
from addons.RatioSimilarity.eFactory import RatioSimilaritySymbolTableFactory

def main(*args):
    manager = ExpressionEvaluatorLocator.getManager();
    manager.registerSymbolTable(RatioSimilaritySymbolTableFactory());
    pass
