x = "    Hello, World!"
print(x[2:5])

#remove os spacos do inicio e fim.
print(x.strip())

#retorna o size da string
print(len(x))

#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#The upper() method returns the string in upper case:
print(a.upper())

#he replace() method replaces a string with another string:
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
print(a.split(",")) # returns ['Hello', ' World!']