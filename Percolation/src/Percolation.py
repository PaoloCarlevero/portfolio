import random
from itertools import chain


class Percolation:

    def __init__(self, num_row: int, num_column: int):
        # creates n-by-n grid, with all sites initially blocked
        self.num_row = num_row
        self.num_column = num_column    
        self.grid = self._create_grid()
        self.connection_array = self._create_connection_array()
        self.size_array = [1]*len(self.connection_array)
        self._connect_top_and_bottom()

    ### Sample managment

    def _create_grid(self):
        grid = []

        for _ in range(self.num_row):
            grid.append([False]*self.num_column)

        return grid

    def open(self,  row, column):
        # Set the specified site as open
        
        self.grid[row-1][column-1] = True

        # Compute the id of the specified site
        site_num = (row-1)*self.num_column + column

        # If the neighboor cell are open, add the union the unions set

        # Left
        if column > 1 and self.grid[row-1][column-2]:
            self.connect(site_num-1, site_num)
        
        # Rigth
        if column < self.num_column and self.grid[row-1][column]:
            self.connect(site_num, site_num+1)

        # Top
        if row > 1 and self.grid[row-2][column-1]:
            self.connect(site_num-self.num_column, site_num)

        # Bottom
        if row < self.num_row and self.grid[row][column-1]:
            self.connect(site_num, site_num+self.num_column)


    def random_site(self):
        row = random.choice(range(1, self.num_row+1))
        column = random.choice(range(1, self.num_column+1))
        return (row, column)

    def is_open(self, row, column) -> bool:
        # is the site (row, col) open?
        return self.grid[row-1][column-1]

    def is_full(self, row, column) -> bool:
        # is the site (row, col) full?
        return not self.grid[row-1][column-1]

    @property
    def num_open_site(self) -> int:
        # returns the number of open sites
        return sum(chain(*self.grid))

    @property
    def percentage_open_site(self) -> float:
        return self.num_open_site/(self.num_row*self.num_column)

    ### Weigthed quick-union

    def percolates(self) -> bool:
        # When does the system percolate?

        while self.root(0) != self.root(self.num_column*self.num_row+1):

            row = random.choice(range(1, self.num_row+1))
            column = random.choice(range(1, self.num_column+1))

            self.open(row, column)

    def _create_connection_array(self):
        # Create an array for every site and set the weight to 1
        # Then set every site as itself as root
        connection_array = [None]*(self.num_column*self.num_row+2)

        for site in range(0, len(connection_array)):
            connection_array[site] = site

        return connection_array
    
    def _connect_top_and_bottom(self):
        for column in range(1, self.num_column+1):
            self.connect(0, column)

        for column in range(self.num_column+1):
            self.connect(self.num_column*self.num_row+1, self.num_column*self.num_row-column)

    def root(self, site):
        while self.connection_array[site] != (site):
            site = self.connection_array[site]
        return site

    def are_connected(self, site_1, site_2):
        return self.root(site_1) == self.root(site_2)

    def connect(self, site_1, site_2):
        root_1 = self.root(site_1)
        root_2 = self.root(site_2)
        if root_1 == root_2:
            return
        elif self.size_array[root_1] > self.size_array[root_2]:
            self.connection_array[root_2] = root_1
            self.size_array[root_1] += self.size_array[root_2]
        else:
            self.connection_array[root_1] = root_2
            self.size_array[root_2] += self.size_array[root_1]


if __name__ == "__main__":
    sample = Percolation(10, 10)

    sample.percolates()
    print(f"{sample.percentage_open_site*100}%")

