#Values assigned to variable x :
x = "MY NAME IS DIVYANSH DIXIT"

#display x:
print(x)
#using operators:
y: str = "hello"
z: str = "world"
r: str = y + z
print(r)
#Multiple strings:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#string array
b = 'I am an idiot'
print(b[6])
var: str = 'yooo'
bar : str = "hooo"
tar :str = var + bar
print(tar)
print (tar[7])
#looping in strings:
for x in "divyansh":
    print(x)
#using function len() for getting touch with length of the string:
c = 'student'
print(len(c))
#using in to check:
word = ' i am a dictonary'
print("am" in word)
#using not keyword:
print("an"not in word)
#using if in not case:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")
#using slicing in between , start, end :
t = 'temporary life'
print(t[2:6])
print(t[:8])
print(t[5:])
#using negative indexing:
b = "Hello, World!"
print(b[-5:-2])
#upper ,lower ,strip ,replace ,split  keyword used to change the formation of words:
u = "  nature is the best  "
print(u.upper())
print(u.lower())
print(u.strip())
print(u.replace("n", "k"))
print(u.split(","))
#using format() for adding string and intergers:
age = 21
text = "My name is Divyansh Dixit, and I am {}"
print(text.format(age))
#backslash mechanism -  use to insert illegal in a string:
pdf = 'It\'s alright.'
print(pdf)
txt = "This will insert one \\ (backslash)."
print(txt)
txt = "Hellot \nWorld!"
print(txt)
txt = "Hello \rWorld!"
print(txt)
txt = "Hello     \t  World!"
print(txt)
txt = "Hello \b World!"
print(txt)
txt = "Hello \fWorld!"
print(txt)
#string methods:
abd = "hi, and welcome to my world."

x = abd.capitalize()

print (x)
abd :str = "hi, and\r welcome to my world."
print(abd)
txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)
txt = "new delhi"

x = txt.center(45)

print(x)
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)
txt = "My name is Tanav "

x = txt.encode()

print(x)
txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"
