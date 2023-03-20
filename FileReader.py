# This file will read a constraint table from a .txt file, store this information in memory and displaying the
# constraint table in the console.

import os
import sys

class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_path = os.path.join(os.path.dirname(__file__), self.file_name)
        self.file = open(self.file_path, "r")
        self.constraint_table = []
        self.constraint_table_size = 0

    def read_file(self):
        for line in self.file:
            self.constraint_table.append(line.strip().split(" "))
        self.constraint_table_size = len(self.constraint_table)
        self.file.close()

    def get_constraint_table(self):
        return self.constraint_table

    def get_constraint_table_size(self):
        return self.constraint_table_size

    def display_constraint_table(self):
        for i in range(self.constraint_table_size):
            print(self.constraint_table[i])

if __name__ == '__main__':
    file_reader = FileReader("ConstraintTable.txt")
    file_reader.read_file()
    file_reader.display_constraint_table()
