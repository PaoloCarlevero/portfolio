from src.PercolationStats import PercolationStats

sample = PercolationStats(trials=1_000, grid = [15, 10])

sample.percolates()

print(sample.result)