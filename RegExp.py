import re

str=input("Enter a string")

Result=re.match(r'\d+',str)

print(Result)
Result=re.findall(r'\w+',str)

print(Result)

Result=re.search(r'\d+',str)
#print(Result.group())
print(Result)

mystr='123Python is the best. 123... Go Python...Go'
Result = re.search(r'\w+',mystr)
print(Result)
Result=re.search(r'\s',mystr)
print(Result)
Result=re.search("Python",mystr)
print("Position of string:",Result.start())

Result=re.search(r'\d+',mystr)
print(Result)

Result=re.search(r'[A-Z]',mystr)
print("Starts with cappital",Result)

emails='My email id is bannuharry@gmail.com. Send me email to kiran.mai@aol.com'
Result=re.search(r'\S+@\S+',emails)
print("Email is:", Result.group())

Result=re.findall(r'\S+@\S+',emails)
print("mails are:",Result)


