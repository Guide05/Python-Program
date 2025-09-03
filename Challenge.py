file = open('input.txt', 'w')
file.write('Trying to master the art of file handling\n')
file.write( 'This is the second line on mastering file handling.\n')
file.write( 'This is the third line.\n')
file.write( 'this is the fourth line.\n')
file.write( 'this is the fifth line.\n')

#reading a file
file = open('input.txt', 'r')
data = file.read() 
print(data)

#counting the number of words in the file
word_count = len(data.split())
print(f'The number of words in the file input.txt is: {word_count}')

#converting the text to uppercase
content_data = data.upper()
print("Text in Uppercase:", content_data)

#writing the processed text and word count output file
file = open('output.txt', 'w')
file.write(content_data)
file.write(f'\n The number of words in the file input.txt is: {word_count}n')

#Printing a success message after the files are created
# this also includes error handling
try:
    file = open('newFile.txt', 'r')
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found.")

finally:
    print("Program successfully executed. Thank You")
    file.close