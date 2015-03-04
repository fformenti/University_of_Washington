import MapReduce
import sys

"""
Relational Join using Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: (i,j) of resulting Matrix
    # value: 
    Matrix_name = record[0]
    i = record[1]
    j = record[2]
    value = record[3]

    if Matrix_name == 'a':
      for k in range(5):
        mr.emit_intermediate((i,k),(Matrix_name,j,value))

    if Matrix_name == 'b':
      for k in range(5):
        mr.emit_intermediate((k,j),(Matrix_name, i,value))

def reducer(key, list_of_values):
  #key: (i,j) position on final matrix
  i = key[0]
  k = key[1]

  row_elements = {}
  col_elements = {}
  for matrix,ref,value in list_of_values:
    if matrix == 'a':
      row_elements[ref] = value
    if matrix == 'b':
      col_elements[ref] = value

  total = 0
  for a,v_row in row_elements.iteritems():
    for b,v_col in col_elements.iteritems():
      if a == b:
        total += v_row * v_col

  mr.emit((i,k,total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
