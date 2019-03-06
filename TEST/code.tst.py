
#is_ltdict(obj)

from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ltd = {0:1,1:2,2:3}
is_ltdict(ltd) == True
ltd = {0:1,2:2,3:3}
is_ltdict(ltd) == False
ltd = {0:1,'1':2,2:3}
is_ltdict(ltd) == False

#json2ltdict(obj,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


json_dict = {'0':'a','1':'b','2':'c'}
json2ltdict(json_dict) == {0:'a',1:'b',2:'c'}


#to_json(ltd,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


ltd = {0:'a',1:'b',2:'c'}
to_json(ltd) == {'1': 'b', '2': 'c', '0': 'a'}


#list2ltdict(array,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


array = ['a','b','c']
list2ltdict(array) == {0: 'a', 1: 'b', 2: 'c'}


#tuple2ltdict(fixed_array,**kwargs)

from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


t = ('a','b','c')
tuple2ltdict(t) == {0: 'a', 1: 'b', 2: 'c'}

#set2ltdict(this_set,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


s = {'a','b','c'}
set2ltdict(s)


#to_list(ltd,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ltd = {0: 'a', 1: 'b', 2: 'c'}
to_list(ltd) == ['a', 'b', 'c']

#to_tuple(ltd,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


ltd = {0: 'a', 1: 'b', 2: 'c'}
to_tuple(ltd) == ('a', 'b', 'c')

#to_set(ltd,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


ltd = {0: 'a', 1: 'b', 2: 'c'}
to_set(ltd) == {'b', 'c', 'a'}

#extend(ltd1,ltd2,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ltd1 = {0: 'a', 1: 'b', 2: 'c'}
ltd2 = {0: 'd', 1: 'e', 2: 'f'}
extend(ltd1,ltd2) == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'}

#prextend(ltd1,ltd2,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


ltd1 = {0: 'a', 1: 'b', 2: 'c'}
ltd2 = {0: 'd', 1: 'e', 2: 'f'}
prextend(ltd1,ltd2) == {0: 'd', 1: 'e', 2: 'f', 3: 'a', 4: 'b', 5: 'c'}

#concat(ltd1,ltd2,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


ltd1 = {0: 'a', 1: 'b', 2: 'c'}
ltd2 = {0: 'd', 1: 'e', 2: 'f'}
concat(ltd1,ltd2) == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'}


#first_continuous_indexes_slice(ltd,value,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
first_continuous_indexes_slice(ltd,'c') == [2, 3]

#last_continuous_indexes_slice(ltd,value,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
last_continuous_indexes_slice(ltd,'c') == [8, 9]

#all_continuous_indexes_slices_array(ltd,value,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
all_continuous_indexes_slices_array(ltd,'c') == [[2, 3], [5], [8, 9]]

#indexes_array(ltd,value,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
indexes_array(ltd,'c') == [2, 3, 5, 8, 9]

#first_index(ltd,value,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
first_index(ltd,'c') == 2

#last_index(ltd,value,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
last_index(ltd,'c') == 9

#append(ltd,value,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ltd = {0: 'a', 1: 'b', 2: 'c'}
append(ltd,'d') == {0: 'a', 1: 'b', 2: 'c', 3: 'd'}


#prepend(ltd,value,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ltd = {0: 'a', 1: 'b', 2: 'c'}
prepend(ltd,'d') == {0: 'd', 1: 'a', 2: 'b', 3: 'c'}

#clear(ltd,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ltd = {0: 'a', 1: 'b', 2: 'c'}
clear(ltd) == {}

#insert(ltd,index,value,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


ltd = {0: 'a', 1: 'b', 2: 'c'}
insert(ltd,1,'d') == {0: 'a', 1: 'd', 2: 'b', 3: 'c'}

#insert_ltdict(ltd1,index,ltd2,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


ltd1 = {0: 'a', 1: 'b', 2: 'c'}
ltd2 = {0: 'd', 1: 'e', 2: 'f'}
insert_ltdict(ltd1,1,ltd2) == {0: 'a', 1: 'd', 2: 'e', 3: 'f', 4: 'b', 5: 'c'}

#include(ltd,value,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


ltd = {0: 'a', 1: 'b', 2: 'c'}
include(ltd,'c') == True

#count(ltd,value,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
count(ltd,'c') == 5

#pop(ltd,index,**kwargs)

from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ltd = {0: 'a', 1: 'b', 2: 'c'}
pop(ltd,1) == 'b'
ltd == {0: 'a', 1: 'c'}

#pop_range(ltd,start,end,**kwargs)

from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
pop_range(ltd,1,7) == {0: 'b', 1: 'c', 2: 'c', 3: 'd', 4: 'c', 5: 'e', 6: 'f'}
ltd == {0: 'a', 1: 'c', 2: 'c'}


#pop_seqs(ltd,seqs_set,**kwargs)

from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
seqs_set = {2,5,8}
pop_seqs(ltd,seqs_set) == {0: 'c', 1: 'c', 2: 'c'}
ltd == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'c'}


#remove_first(ltd,value,**kwargs)

from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
remove_first(ltd,'c') == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'c', 5: 'e', 6: 'f', 7: 'c', 8: 'c'}
ltd == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'c', 5: 'e', 6: 'f', 7: 'c', 8: 'c'}

#remove_last(ltd,value,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
remove_last(ltd,'c') == {0: 'a', 1: 'b', 2: 'c', 3: 'c', 4: 'd', 5: 'c', 6: 'e', 7: 'f', 8: 'c'}
ltd == {0: 'a', 1: 'b', 2: 'c', 3: 'c', 4: 'd', 5: 'c', 6: 'e', 7: 'f', 8: 'c'}

#remove_all(ltd,value,**kwargs)

from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
remove_all(ltd,'c') == {0: 'a', 1: 'b', 2: 'd', 3: 'e', 4: 'f'}
ltd == {0: 'a', 1: 'b', 2: 'd', 3: 'e', 4: 'f'}


#reverse(ltd,**kwargs)

from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
reverse(ltd) == {0: 'c', 1: 'c', 2: 'f', 3: 'e', 4: 'c', 5: 'd', 6: 'c', 7: 'c', 8: 'b', 9: 'a'}
ltd == {0: 'c', 1: 'c', 2: 'f', 3: 'e', 4: 'c', 5: 'd', 6: 'c', 7: 'c', 8: 'b', 9: 'a'}


#sort(ltd,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir


ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
sort(ltd) == {0: 'a', 1: 'b', 2: 'c', 3: 'c', 4: 'c', 5: 'c', 6: 'c', 7: 'd', 8: 'e', 9: 'f'}
ltd == {0: 'a', 1: 'b', 2: 'c', 3: 'c', 4: 'c', 5: 'c', 6: 'c', 7: 'd', 8: 'e', 9: 'f'}


#comprise(ltd1,ltd2,**kwargs)
from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ltd1 = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f'}
ltd2 = {0:'a',1:'b',2:'c'}
comprise(ltd1,ltd2) == True
ltd3 = {0:'c',1:'d',2:'e'}
comprise(ltd1,ltd3) == False
comprise(ltd1,ltd3,strict=False) == True


#naturalize_intkeydict(ikd)

from ltdict.ltdict import *
from xdict.jprint import pobj,pdir

ikd = {3:'a',1:'b',2:'c',11:'d',0:'e',50:'f'}
naturalize_intkeydict(ikd) == {0: 'e', 1: 'b', 2: 'c', 3: 'a', 4: 'd', 5: 'f'}

