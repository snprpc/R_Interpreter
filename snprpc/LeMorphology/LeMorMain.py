__author__ = '1'

from LeMorphology.LeCode import *
from LeMorphology.LeMorAnalysis import *

code = Code()
codes = code.getCode('F://simple.txt')
print(codes)
test = MorAnalysis()
print(test.getResult(codes))

