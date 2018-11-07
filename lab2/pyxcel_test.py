import pyexcel 
from collections import OrderedDict

a_list_of_dic =[
    OrderedDict({
        "Name":1,
        "Age":"luabom"
    }),
    OrderedDict({
        "Name":3,
        "Age":4
    })
]


#list comprehension


#
pyexcel.save_as(records = a_list_of_dic,dest_file_name="your_file.xlsx")