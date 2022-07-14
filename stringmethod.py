#python string method
 # capatalize()
str ='i love my India'
print(str.capitalize())

#center()
str ='i love my India'
print(str.center(24,'*'))

#casefold()
str ='pYtHon'
print(str.casefold())

#count()
str1 ="Python is asome, isn't it?"
substring ="is"
print(str1.count(substring))

str1 ="Python is asome, isn't it?"
substring ="is"
print(str1.count(substring,8,25))

#Suffix()
#without start & ends  parameters

text ="Python is easy to learn."
result = text.endswith('to learn')
#returns False
print(result)

result = text.endswith('to learn.')
#returns True
print(result)

result =text.endswith('Python is easy to learn.')
#returns True
print(result)

