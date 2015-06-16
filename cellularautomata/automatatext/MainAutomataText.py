# -*- coding: utf-8 -*-

'''
Created on 11/03/2015

@author: Nicoli
'''
from src.cellularautomata.automatatext.ParserImgToText import ParserNist
from src.cellularautomata.automatatext.AutomataText import AutomataText
from src.cellularautomata.rulenumber.RuleNumber import RuleNumber
#from src.cellularautomata.totalisticcode.TotalisticCodePicture import TotalisticCodePicture

if __name__ == '__main__':
    
    elementar = [72, 136, 103, 91, 30, 73, 101, 105, 129, 137, 161, 183, 169, 214, 225, 45, 26, 57, 62, 89]
    
    for i in elementar: 
    
        rule = RuleNumber(i)
        ruletext = AutomataText(20, 50000, rule, 1)
        ruletext.setFile()
        ParserNist(str(ruletext.autocel.rule))

        print(str(i) + "Operação terminada" )
     
#==============================================================================
#    b = TotalisticCodePicture(3, 3, 600, 3, 1)
#    b.setImage()
#     
#    x= AutomataText(b.image, b.automata.k, b.height, b.width)
# 
#    x.imgToTxt(b.automata.rule)
#==============================================================================
