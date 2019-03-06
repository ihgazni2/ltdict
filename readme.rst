.. contents:: Table of Contents
   :depth: 5


*ltdict*
========

- list style dict,

Installation
------------
    ::

    $ pip3 install ltdict


License
-------

- MIT




Usage
=====

0. is_ltdict(obj)
-----------------

    ::
    
        
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ltd = {0:1,1:2,2:3}
        is_ltdict(ltd) == True
        ltd = {0:1,2:2,3:3}
        is_ltdict(ltd) == False
        ltd = {0:1,'1':2,2:3}
        is_ltdict(ltd) == False

.. image:: /docs/images/is_ltdict.svg

1. json2ltdict(obj,**kwargs)
----------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        json_dict = {'0':'a','1':'b','2':'c'}
        json2ltdict(json_dict) == {0:'a',1:'b',2:'c'}
        
        
        

.. image:: /docs/images/json2ltdict.svg

2. to_json(ltd,**kwargs)
------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        ltd = {0:'a',1:'b',2:'c'}
        to_json(ltd) == {'1': 'b', '2': 'c', '0': 'a'}
        
        
        

.. image:: /docs/images/to_json.svg

3. list2ltdict(array,**kwargs)
------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        array = ['a','b','c']
        list2ltdict(array) == {0: 'a', 1: 'b', 2: 'c'}
        
        
        

.. image:: /docs/images/list2ltdict.svg

4. tuple2ltdict(fixed_array,**kwargs)
-------------------------------------

    ::
    
        
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        t = ('a','b','c')
        tuple2ltdict(t) == {0: 'a', 1: 'b', 2: 'c'}

.. image:: /docs/images/tuple2ltdict.svg

5. set2ltdict(this_set,**kwargs)
--------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        s = {'a','b','c'}
        set2ltdict(s)
        
        
        

.. image:: /docs/images/set2ltdict.svg

6. to_list(ltd,**kwargs)
------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ltd = {0: 'a', 1: 'b', 2: 'c'}
        to_list(ltd) == ['a', 'b', 'c']

.. image:: /docs/images/to_list.svg

7. to_tuple(ltd,**kwargs)
-------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        ltd = {0: 'a', 1: 'b', 2: 'c'}
        to_tuple(ltd) == ('a', 'b', 'c')

.. image:: /docs/images/to_tuple.svg

8. to_set(ltd,**kwargs)
-----------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        ltd = {0: 'a', 1: 'b', 2: 'c'}
        to_set(ltd) == {'b', 'c', 'a'}

.. image:: /docs/images/to_set.svg

9. extend(ltd1,ltd2,**kwargs)
-----------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ltd1 = {0: 'a', 1: 'b', 2: 'c'}
        ltd2 = {0: 'd', 1: 'e', 2: 'f'}
        extend(ltd1,ltd2) == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'}

.. image:: /docs/images/extend.svg

10. prextend(ltd1,ltd2,**kwargs)
--------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        ltd1 = {0: 'a', 1: 'b', 2: 'c'}
        ltd2 = {0: 'd', 1: 'e', 2: 'f'}
        prextend(ltd1,ltd2) == {0: 'd', 1: 'e', 2: 'f', 3: 'a', 4: 'b', 5: 'c'}

.. image:: /docs/images/prextend.svg

11. concat(ltd1,ltd2,**kwargs)
------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        ltd1 = {0: 'a', 1: 'b', 2: 'c'}
        ltd2 = {0: 'd', 1: 'e', 2: 'f'}
        concat(ltd1,ltd2) == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'}
        
        
        

.. image:: /docs/images/concat.svg

12. first_continuous_indexes_slice(ltd,value,**kwargs)
------------------------------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        first_continuous_indexes_slice(ltd,'c') == [2, 3]

.. image:: /docs/images/first_continuous_indexes_slice.svg

13. last_continuous_indexes_slice(ltd,value,**kwargs)
-----------------------------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        last_continuous_indexes_slice(ltd,'c') == [8, 9]

.. image:: /docs/images/last_continuous_indexes_slice.svg

14. all_continuous_indexes_slices_array(ltd,value,**kwargs)
-----------------------------------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        all_continuous_indexes_slices_array(ltd,'c') == [[2, 3], [5], [8, 9]]

.. image:: /docs/images/all_continuous_indexes_slices_array.svg

15. indexes_array(ltd,value,**kwargs)
-------------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        indexes_array(ltd,'c') == [2, 3, 5, 8, 9]

.. image:: /docs/images/indexes_array.svg

16. first_index(ltd,value,**kwargs)
-----------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        first_index(ltd,'c') == 2

.. image:: /docs/images/first_index.svg

17. last_index(ltd,value,**kwargs)
----------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        last_index(ltd,'c') == 9

.. image:: /docs/images/last_index.svg

18. append(ltd,value,**kwargs)
------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ltd = {0: 'a', 1: 'b', 2: 'c'}
        append(ltd,'d') == {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
        
        
        

.. image:: /docs/images/append.svg

19. prepend(ltd,value,**kwargs)
-------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ltd = {0: 'a', 1: 'b', 2: 'c'}
        prepend(ltd,'d') == {0: 'd', 1: 'a', 2: 'b', 3: 'c'}

.. image:: /docs/images/prepend.svg

20. clear(ltd,**kwargs)
-----------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ltd = {0: 'a', 1: 'b', 2: 'c'}
        clear(ltd) == {}

.. image:: /docs/images/clear.svg

21. insert(ltd,index,value,**kwargs)
------------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        ltd = {0: 'a', 1: 'b', 2: 'c'}
        insert(ltd,1,'d') == {0: 'a', 1: 'd', 2: 'b', 3: 'c'}

.. image:: /docs/images/insert.svg

22. insert_ltdict(ltd1,index,ltd2,**kwargs)
-------------------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        ltd1 = {0: 'a', 1: 'b', 2: 'c'}
        ltd2 = {0: 'd', 1: 'e', 2: 'f'}
        insert_ltdict(ltd1,1,ltd2) == {0: 'a', 1: 'd', 2: 'e', 3: 'f', 4: 'b', 5: 'c'}

.. image:: /docs/images/insert_ltdict.svg

23. include(ltd,value,**kwargs)
-------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        ltd = {0: 'a', 1: 'b', 2: 'c'}
        include(ltd,'c') == True

.. image:: /docs/images/include.svg

24. count(ltd,value,**kwargs)
-----------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        count(ltd,'c') == 5

.. image:: /docs/images/count.svg

25. pop(ltd,index,**kwargs)
---------------------------

    ::
    
        
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ltd = {0: 'a', 1: 'b', 2: 'c'}
        pop(ltd,1) == 'b'
        ltd == {0: 'a', 1: 'c'}

.. image:: /docs/images/pop.svg

26. pop_range(ltd,start,end,**kwargs)
-------------------------------------

    ::
    
        
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        pop_range(ltd,1,7) == {0: 'b', 1: 'c', 2: 'c', 3: 'd', 4: 'c', 5: 'e', 6: 'f'}
        ltd == {0: 'a', 1: 'c', 2: 'c'}
        
        
        

.. image:: /docs/images/pop_range.svg

27. pop_seqs(ltd,seqs_set,**kwargs)
-----------------------------------

    ::
    
        
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        seqs_set = {2,5,8}
        pop_seqs(ltd,seqs_set) == {0: 'c', 1: 'c', 2: 'c'}
        ltd == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'c'}
        
        
        

.. image:: /docs/images/pop_seqs.svg

28. remove_first(ltd,value,**kwargs)
------------------------------------

    ::
    
        
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        remove_first(ltd,'c') == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'c', 5: 'e', 6: 'f', 7: 'c', 8: 'c'}
        ltd == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'c', 5: 'e', 6: 'f', 7: 'c', 8: 'c'}

.. image:: /docs/images/remove_first.svg

29. remove_last(ltd,value,**kwargs)
-----------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        remove_last(ltd,'c') == {0: 'a', 1: 'b', 2: 'c', 3: 'c', 4: 'd', 5: 'c', 6: 'e', 7: 'f', 8: 'c'}
        ltd == {0: 'a', 1: 'b', 2: 'c', 3: 'c', 4: 'd', 5: 'c', 6: 'e', 7: 'f', 8: 'c'}

.. image:: /docs/images/remove_last.svg

30. remove_all(ltd,value,**kwargs)
----------------------------------

    ::
    
        
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        remove_all(ltd,'c') == {0: 'a', 1: 'b', 2: 'd', 3: 'e', 4: 'f'}
        ltd == {0: 'a', 1: 'b', 2: 'd', 3: 'e', 4: 'f'}
        
        
        

.. image:: /docs/images/remove_all.svg

31. reverse(ltd,**kwargs)
-------------------------

    ::
    
        
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        reverse(ltd) == {0: 'c', 1: 'c', 2: 'f', 3: 'e', 4: 'c', 5: 'd', 6: 'c', 7: 'c', 8: 'b', 9: 'a'}
        ltd == {0: 'c', 1: 'c', 2: 'f', 3: 'e', 4: 'c', 5: 'd', 6: 'c', 7: 'c', 8: 'b', 9: 'a'}
        
        
        

.. image:: /docs/images/reverse.svg

32. sort(ltd,**kwargs)
----------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        
        ltd = {0:'a',1:'b',2:'c',3:'c',4:'d',5:'c',6:'e',7:'f',8:'c',9:'c'}
        sort(ltd) == {0: 'a', 1: 'b', 2: 'c', 3: 'c', 4: 'c', 5: 'c', 6: 'c', 7: 'd', 8: 'e', 9: 'f'}
        ltd == {0: 'a', 1: 'b', 2: 'c', 3: 'c', 4: 'c', 5: 'c', 6: 'c', 7: 'd', 8: 'e', 9: 'f'}
        
        
        

.. image:: /docs/images/sort.svg

33. comprise(ltd1,ltd2,**kwargs)
--------------------------------

    ::
    
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ltd1 = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f'}
        ltd2 = {0:'a',1:'b',2:'c'}
        comprise(ltd1,ltd2) == True
        ltd3 = {0:'c',1:'d',2:'e'}
        comprise(ltd1,ltd3) == False
        comprise(ltd1,ltd3,strict=False) == True
        
        
        

.. image:: /docs/images/comprise.svg

34. naturalize_intkeydict(ikd)
------------------------------

    ::
    
        
        from ltdict.ltdict import *
        from xdict.jprint import pobj,pdir
        
        ikd = {3:'a',1:'b',2:'c',11:'d',0:'e',50:'f'}
        naturalize_intkeydict(ikd) == {0: 'e', 1: 'b', 2: 'c', 3: 'a', 4: 'd', 5: 'f'}
        
        
        

.. image:: /docs/images/naturalize_intkeydict.svg

