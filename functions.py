FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """
    Read a text file and return list of todos
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write todo items in todo list
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello from functions inside")