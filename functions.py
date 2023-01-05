FILEPATH = 'todos.txt'

def get_todos(filename=FILEPATH):
    """Read a text file and return a list of to-do items"""
    with open(filename, 'r') as file:
            todos_local = file.readlines()
    return todos_local
     

def write_todos(todos_arg, filename=FILEPATH):
    """write the to-do items list in the txt file"""
    with open(filename, 'w') as file:
            file.writelines(todos_arg)
    return  

if __name__ == "__main__":
        print(get_todos())