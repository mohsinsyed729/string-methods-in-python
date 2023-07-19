# strings are immutable
a="mohsin"
print(len(a))
#we can convert it in upper/lower case
print(a.upper())
print(a.lower())

#rstrip()
b="syed!"
print(b.upper())
print(b.lower())
print(b.rstrip("!"))

# replace()
print(a.replace("mohsin","syed mohsin aijaz"))

# split()
c="syed mohsin aijaz"
print(c.split(" "))

# capitalize()        (first letter)
d="mohsin"
print(d.capitalize())
d1="moHsin"
print(d1.capitalize())

# center
e="syed mohsin aijaz"
print(e.center(50)) #adjust by number

# count
print(c.count("i"))

# endswith
print(e.endswith("z"))
print(e.endswith("aijaz"))
print(e.endswith("syed")) #false

