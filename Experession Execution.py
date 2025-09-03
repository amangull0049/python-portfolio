# string and numeric can operate together with "*"
a,b = 2,3
txt = "@"
print(a*txt*b,"\n")

# string and string can operate together with "+"
c,d = "2",3
txt = "@"
print ((c+txt) * d,"\n") 

# numeric value operate with all arithmetic operator
e,f = 2,3
g = 6
print(e + f * g,"\n")

# arithmetic expression with integer and float will result in float
x,y = 19,7.7
z = x * y
print(z,"\n")

# result of division operator with two integers will be float
h,i = 1,2
j = h/i
print(j,"\n")
