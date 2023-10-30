from vis import PrimVisualizer as Visualizer
import data_sample_cities as dsc

# adjacency matrix - array of array
def build_graph():
  global graph
  graph = {u: dict() for u in range(n_cities)}
  for u,v,w in edges:
    graph[u][v] = w
    graph[v][u] = w
  print(graph)
  print_adj_matrix()

def print_adj_matrix():
  for u in range(n_cities):
    for v in range(n_cities):
      w = f'{graph[u][v]:5d}' if v in graph[u] else ' ....'
      print(w, end='')
    print()
  print()

def main():
  global n_cities
  n_cities = len(cities)

  build_graph()

  start_city_index = 0
  print(f'{n_cities} cities, starts from {cities[start_city_index]}')

  global weights
  weights = dict()
  weights[start_city_index] = 0
  print(weights)

if __name__ == '__main__':
  vis = Visualizer('Minimum Spanning Tree - Prim')
  idx = 0
  while True:
    cities, edges = dsc.cities, dsc.edges
    vis.setup(vis.get_main_module())
    vis.draw()
    main()
    again = vis.end()
    if not again: break
    if vis.restart_lshift:
      dsc.next()
    elif vis.restart_rshift:
      dsc.random()
