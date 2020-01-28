print("hola Mundo")
print ("hola", "mundo")


pes=input("quien es el pes?")
type(pes)
print(pes)

llist=(range(10))
print(llist)

llistaA=[x*2 for x in range(10)]
print(llistaA)

llista=[x**2 for x in range(10)]
print(llista)

llistaD=[x**2 for x in range(10) if x%2==0]
print(llistaD)



n = 6
str = "Tinc {} anys".format(n)
print(str)

for pepe in range(11):
    print(pepe)

print("------------------------")


llis = ["a","b","c","d"]
print(llis[1])
print(llis[-3])
var1 = llis[0:2]
var2 = llis[0:4:2]
print(var1)
print(var2)

age=13
print('kid' if age>5 else 'hola')



print("------------------------")


def inc(x):
    return x+1

def dec(c):
    return c+1

def operate(func,x):
    result=func(x)
    return result

print(operate(dec,3))
print(operate(inc,3))


print("------------------------")

def is_called():
    def is_returned():
        print("Hello")
    return is_returned
new = is_called()
#Outputs "Hello"
new()