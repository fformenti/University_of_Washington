import MapReduce
import sys

"""
Inverted Index using Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person
    # value: friend
    person = record[0]
    friend = record[1]        
    mr.emit_intermediate(person, friend)
    mr.emit_intermediate(friend, person)

def reducer(key, list_of_values):
    # key: person
    # value: friend

    for friend in list_of_values:
        if list_of_values.count(friend) == 1:
            mr.emit((key, friend))


inputdata = open('C:/Users/Cicero/Documents/Estudos/University of Washigton/Introduction to Data Science/assignment3/data/friends.json')
mr.execute(inputdata, mapper, reducer)
