import MapReduce
import sys

"""
Social Network friend count using Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    key = record[0]
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    # key: person
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))


inputdata = open('C:/Users/Cicero/Documents/Estudos/University of Washigton/Introduction to Data Science/assignment3/data/friends.json')
mr.execute(inputdata, mapper, reducer)
