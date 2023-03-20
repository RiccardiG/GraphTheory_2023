# This file will contain the Graph class. This class will be used to create a graph object from the constraint table.
# This class will contain all the methods to check whether the graph is a valid scheduling graph.

import numpy as np
import pandas as pd

class Graph:
    def __init__(self, constraint_table):
        self.constraint_table = constraint_table
        self.constraint_table_size = len(constraint_table)
        self.graph = np.zeros((self.constraint_table_size, self.constraint_table_size), dtype=int)

    def get_graph(self):
        return self.graph

    def get_graph_size(self):
        return self.constraint_table_size

    def create_graph(self):
        # From the constraint table, we will create a graph.
        for i in range(self.constraint_table_size):
            # 





    def display_graph(self):
        print(pd.DataFrame(self.graph))

    def is_valid_graph(self):
        for i in range(self.constraint_table_size):
            for j in range(self.constraint_table_size):
                if self.graph[i][j] == 1 and self.graph[j][i] == 1:
                    return False
        return True