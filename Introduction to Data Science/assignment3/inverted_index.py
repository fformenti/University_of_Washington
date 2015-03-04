import MapReduce
import sys

"""
Inverted Index using Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    #for k in key:
    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    doc_list = []
    for v in list_of_values:
      doc_list.append(v)
    # removing duplicates
    doc_set = set(doc_list)
    doc_list = list(doc_set)
    mr.emit((key, doc_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
