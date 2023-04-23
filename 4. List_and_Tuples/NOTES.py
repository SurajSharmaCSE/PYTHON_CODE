#Delcare a List==========================================
friends=["Suraj","Sooraj","Suray","rohan"]

#List indexing
l1=[7,9,"Suraj"]
l1[0]  #7
l1[1]  #9

#List Methods
l2=[1,8,7,2,21,15]

# l2.sort()
# l2.reverse()
# l2.append(11)
#insert(index,value) 
# l2.insert(3,88) 

#pop(index) 
# l2.pop(3)

#remove(value)
l2.remove(15)
print(l2)

#Declare a Tuple(Tuple is immutable data means can't change)===========================================
# t=() Empty tuple
# t=(1,) = tuple with only one element 
# t=(1,2,3) = tupke with more than one element

#Tuple method
t=(1,1,7,2)
# rs=t.count(1)
rs=t.index(1) #it return first occurence of 1
print(rs)



