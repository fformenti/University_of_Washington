import MapReduce
import sys

"""
Relational Join using Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: join field
    # value: concatenation of records for the two tables
    key = record[1]
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: join field
    # value: concatenation of records for the two tables
    order_list = []
    item_list = []
    for value in list_of_values:
        if value[0] == 'order':
            order_list.append(value)
        else:
            item_list.append(value)

    for order in order_list:
        for item in item_list:
            mr.emit(order + item)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
