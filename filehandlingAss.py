


#Reads the content of a file and returns it.

def read_file(file_path):

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    except IOError:
        print(f"Error: The file '{file_path}' cannot be read.")
        return None

#Writes the modified content to a new file.
def write_file(file_path, content):
    
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Successfully written to '{file_path}'.")
    except IOError:
        print(f"Error: The file '{file_path}' cannot be written.")

def modify_content(content):
    
    return content.upper()

def main():
    input_file = input("Please enter the filename to read: ")
    content = read_file(input_file)
    
    if content is not None:
        modified_content = modify_content(content)
        output_file = input("Please enter the filename to write the modified content: ")
        write_file(output_file, modified_content)


def main():
    input_file = input("Please enter the filename to read: ")
    content = read_file(input_file)
    
    if content is not None:
        modified_content = modify_content(content)
        output_file = input("Please enter the filename to write the modified content: ")
        write_file(output_file, modified_content)

if __name__ == "__main__":
    main()