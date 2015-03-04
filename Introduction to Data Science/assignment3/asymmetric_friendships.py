import MapReduce
import sys

"""
Asymmetric Friendships using Python MapReduce Framework
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

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
