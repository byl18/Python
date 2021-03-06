list2 = [1,2,1,3,8]
list1=list2.copy()
tuples=tuple(list2)
print(type(list1),type(list2),type(tuples),any(list1))

#list2[1:2]=[]
#for content in mylist+list2:
#    print(content,end="\n")