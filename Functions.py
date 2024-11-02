FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items """
    with open(filepath, "r") as Prev_file:
        todos_local = Prev_file.readlines()
    return todos_local


def write_todos(todos_list, filepath=FILEPATH):
    """ Write a to-do items list in a text file. """
    with open(filepath, "w") as New_file:
        New_file.writelines(todos_list)


print(__name__)

if __name__ == "__main__":
    print("Hello from Functions")
    print(get_todos())
