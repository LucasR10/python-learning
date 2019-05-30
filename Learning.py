#comentantario pytho
print("Hello, World!")
if 5 > 3:
    print("ok, deu certo.")

#docstring
""" this is a multiline docstring."""

x = 75;
print("valor de x ->",x);
z = 10;
print(type(x))
print("valor de y ->",x);
print(x + z);

#sao tipos de numerico in python
x1 = 1    # int
y1 = 2.8  # float
z1 = 1j   # complex

print(type(x1))
print(type(y1))
print(type(z1))

#Python Casting

#int cast
castX =  int(1) # x will be 1.0
castY=  int(2.8) # x will be 2.8
castZ =  int("1")# x will be 1.0

#float cast
castX1 = float(1)     # x will be 1.0
castY1 = float(2.8)   # y will be 2.8
castZ1 = float("3")   # z will be 3.0
castW1 = float("4.2") # w will be 4.2

#str cast
cx = str("s1") # x will be 's1'
cy = str(2)    # y will be '2'
cz = str(3.0)  # z will be '3.0'

#obter um character de uma position 1 (relembre que a prmeira esta na posicai  0):

a = "Hello, World!"
print(a[1]) #posicao 1 -> e
print(a[5]) #posicao 5 -> ,