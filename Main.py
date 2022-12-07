def read_file(file_name):
   
    """ Reads in a file.
    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    f = open(file_name +'.txt')
    f = f.read()
    print(f)
    return f
def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    list = []
    print(file_name)
    f = open(file_name +'.txt')
    # f = open(file_name)
    data = f.readlines()
    for i in data:
        list.append(i)
#    list = data.split("\n")
    
    #print(list)

   # f.close()

    return list
    data_into_list = data.split("\n")
    
def write_first_line_to_file(file_contents, output_filename):
    

    """ Writes the first line of a string to a file.

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    #print('------!!!!',file_contents)
    c = file_contents
    d = file_contents.split('\n')

    #print('-------!!!!!!!!!!!',d[0])
    a = open(output_filename,'w')
    a.write(d[0])
    a.close()
    e  =open(output_filename,'r')
    e = e.read()
    print(e)
    #a = open(output_filename,'r')
    #print(a.read())


def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
        
    list =[]
    
    f = open(file_name +".txt")
    a = f.readlines()
    list =a[1::2]
    print(list)
    return list

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order
    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    for line in reversed(open(file_name +".txt").readlines()):
        list1=[]
        list1=line.rstrip()
        
        print(list1)
    return list1
        
def main():
    file_name = 'sampletext'
    file_contents = read_file(file_name)
    print(read_file_into_list(file_name))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines(file_name))
    print(read_file_in_reverse(file_name))

if __name__ == "__main__":
    main()