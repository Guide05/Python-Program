from importlib.resources import contents


file = open('newFile.pdf', 'w')
file.write('Hello World, this is amazing')

#reading a file
file = open('newFile.pdf', 'r')
data = file.read()
print(data)

#Appending to a file
file = open('newFile.pdf', 'a')
file.write('Today its very sunny')

#Error Handling
try:
    file = open('newFile.txt', 'r')
    data = file.read()
    print(contents)
except FileNotFoundError:
    print("File not found.")

finally:
    print("Program successfully executed")
    file.close