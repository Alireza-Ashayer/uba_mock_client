import sys
import os
import random
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-r", "--rate", action="store", dest="rate")
(options, args) = parser.parse_args()

rate = options.rate

if rate is None:
    raise ValueError("Please specify rate [-r]")



