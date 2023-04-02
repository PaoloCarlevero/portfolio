import numpy as np
from matplotlib import pyplot as plt

from src.Percolation import Percolation


class PercolationStats:
    
    def __init__(self, trials: int = 100, grid: int|list = 100):
        self.trials = trials
        self.grid = grid
        self.percolation_results = np.empty(trials, dtype=float)

    def percolates(self):
        print("Percolating")
        if isinstance(self.grid, list):
            rows, columns = self.grid
        else:
            rows = columns = self.grid

        for i in range(self.trials):
            if i % (self.trials/20) == 0:
                print(f"{i*100/self.trials}%")
            percolation = Percolation(rows, columns)
            percolation.percolates()

            #print(percolation.percentage_open_site)
            self.percolation_results[i] = percolation.percentage_open_site

    @property
    def mean(self) -> float:
        return round((sum(self.percolation_results)/self.trials)*100, 2)

    @property
    def confidence_intervall(self) -> float:
        return round((1.96*(np.std(self.percolation_results) / self.trials**0.5))*100, 2)

    @property
    def result(self):
        return f"{self.mean} \u00B1 {self.confidence_intervall}" 
