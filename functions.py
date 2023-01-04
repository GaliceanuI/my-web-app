FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """" Read a text file and return the list of
     to-do items.
     """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local                                            # use return if the function actually has an output.


def write_todos(todos_arg, filepath=FILEPATH):          #you can have both default and nondefault params but the order has to be 1st = nondefault 2nd...100th = default
    """ Write a to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

#print("i am outside!")                                          # #prints if you want to run the file indirectly
if __name__ == "__main__":                                      # prints if you want to run the file directly
    print("Hello")