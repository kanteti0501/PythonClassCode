from functools import reduce

Numbers = [1,2,3,4,5,6,7,8,9,22,24,36,77,34,89]
even = list(filter(lambda x:x%2!=0,Numbers))
print(even)

fruits={'apple','banana','orange','kiwi','blueberry','apricot','peach','avacado'}
afruits = set(filter(lambda f:f.startswith('a'),fruits))
print(afruits)

nos=(9,11,32,12,77)
sqrs=set(map(lambda x:x*x, nos))
print(sqrs)

str1=['kiran','harry','jai','hima']
upstr=list(map(str.upper,str1))
print(upstr)

lst1={'Kiran','hi','9087.7866'}
lst2={'Brocoli','Carrot','Beans','Peas'}
newlist=set(map(lambda x, y:x+y,lst1,lst2))
print(newlist)

nos=[1,2,3,4,5,6]
newset=list(map(lambda x: x*x, filter(lambda y:y%2==0,nos) ))
print(newset)

newset=[x*2 for x in nos if x%2==0]
print(newset)

newset=reduce(lambda x,y:x+y,nos)
print(newset)