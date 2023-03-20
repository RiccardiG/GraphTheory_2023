# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from FileReader import FileReader
from Graph import Graph

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Let us test the FileReader.py file here. Do not forget to import the file.
    file_reader = FileReader("ConstraintTable.txt")
    file_reader.read_file()
    file_reader.display_constraint_table()
    print_hi("PyCharm")
    # Let us test the Graph.py file here. Do not forget to import the file.
    graph = Graph(file_reader.get_constraint_table())
    graph.create_graph()
    graph.display_graph()
    print(graph.is_valid_graph())



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
