#DATA TYPES

#1.None
a= None
print(a)
print(id(a))
print(type(a))

phone_num = 9405031638
print(phone_num)

#Numeric(int,float,complex)
a = 100
print(type(a))

num = '314'
print(type(num))

#integer to binary & binary to integer
a=25
print(bin(a))

b=20
print(bin(b))

a=120
print(type(a))

a='120'
print(type(a))

age=27
percentage=96.56
print(type(age))
print(type(percentage))

b=0b1111
print(int(b))

c=0b1010
print(int(b))

#Binary to Integer Conversion prefix 0b(zero+lowercase letter 'b')
a=0b1111
print("the type of variable having value",int(a),"is",type(a))

#Binary to Integer Conversion 0B(zero+uppercase letter 'B')
a=-0B1111
print("The type of variable having value",int(a),"is",type(a))

#Integer to Octal & Octal to Integer
#Integer to Octal Conversion oct()
a=23
print("The type of variable having value",oct(a),"is",type(a))

#Octal to Integer Conversion 0o(zero+lowercase letter 'o')
a=0o1111
print("The type of variable having value",int(a),"is",type(a))

#Octal to Integer Conversion 0O(zero+uppercase letter 'O')
a=0O7777
print("The type of variable having value",int(a),"is",type(a))

#Integer to Hexadecimal & Hexadecimal to Integer

##Integer to Hexadecimal Conversion hex()
a=63
print("The type of variable having value",hex(a),"is",type(a))

#Hexadecimal to Integer Conversion 0X(zero+uppercase letter 'X')
a=0XFace
print("The type of variable having value",int(a),"is",type(a))

#Hexadecimal to Integer Conversion 0x(zero+lowercase letter 'x')
a=0xBeef
print("The type of variable having value",int(a),"is",type(a))


print(123123123123123123123123123123123123123123123 +1000)

#Float Data Type

#create a variable with float value.doller price
b=10.2345
print("The type of variable having value",b,"is",type(b))

#Specify the value in Exponetial Form
b=1.2e3
print("The type of variable having value",b,"is",type(b))

b=1.79e308
print("The type of variable having value",b,"is",type(b))

b=1.8e308
print("The type of variable having value",b,"is",type(b))

b=5e-324
print("The type of variable having value",b,"is",type(b))

b=1e-325
print("The type of variable having value",b,"is",type(b))

#complex  Data Type
#com=(a+bj)
#com.real
#com.imag

#create a variable with complex value.
c=100+3j
print("The type of variable having value",c,"is",type(c))

#checking Real & Imaginary part
c=100+3j
print("The real part is",c.real)
print("The Imaginary part is",c.imag)



