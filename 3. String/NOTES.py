#1. we can Write String in 3 way
firstway='Suraj'
secondWay="Suraj"
thirdWay='''Suraj'''

#2.String Slicing 
name="Suraj"
sl=name[0:2]
sl1=name[0:3]
print(sl,sl1)

#3. Slicing with Skip value
word="amazing"
rt=word[1:6:2]
print(rt)

#String Function==================================

#len() function
name="Suraj"
ln=len(name)
print(ln)
#output - 5

#endswith() function
name="Suraj"
check=name.endswith("aj")
print(check)

#count() function
name="Suraj"
print(name.count("S"))

#capitalize() function
name="suraj"
name=name.capitalize()
print(name)

#find(word) finction
name='Suraj'
rs=name.find("r")
print(rs)  #output 2

#replace(oldword, newword ) function
name='Suraj'
name=name.replace("u","oo")
print(name)