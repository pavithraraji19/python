list=[1,'a',"apple"]
print (list)
list.append("bae")
print (list)
list.insert(2,'b')
print (list)
list2=["gfg",["hi","hello"]]
list.append(list2)
print(list)
indi=list.index('bae')
print(indi)
indi2=list2.index('gfg')
print(indi2)
list.insert(3,"oye")
print(list)
list3=["kya",'re']
list.append(list3)
print(list)
list.remove('bae')
print (list)
list4=[81,7,2,93,455,5,5,5]
list4.sort()
print (list4)
counts=list4.count(5)
print (counts)
list4=[81,7,2,93,455,5,5,5]
list4.reverse()
print(list4)
list5=list4.copy()
print(list5)
list5.pop(5)
print(list5)
list5.clear()
print (list5)