from src.dijkstra import Dijkstra

expression = '(4 * 20) +  45 / 7 - (35 * 4 / 20)'

dj = Dijkstra()
print(dj.solve(expression))
print(eval(expression))