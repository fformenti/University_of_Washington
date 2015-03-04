import MapReduce
import sys

"""
Inverted Index using Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    nucleotid_chain = record[1]
    trimmed = nucleotid_chain[:-10]
    mr.emit_intermediate(trimmed, "-")

def reducer(key, list_of_values):
    mr.emit(key)


inputdata = open('C:/Users/Cicero/Documents/Estudos/University of Washigton/Introduction to Data Science/assignment3/data/dna.json')
mr.execute(inputdata, mapper, reducer)
