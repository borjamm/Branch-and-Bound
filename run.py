# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
print("-------------------------------------------------------------------------------------------------------")
print("Anchura:")
print(search.breadth_first_graph_search(ab).path())
print("-------------------------------------------------------------------------------------------------------")
print("Profundidad:")
print(search.depth_first_graph_search(ab).path())
print("-------------------------------------------------------------------------------------------------------")
print("Ramificación y salto sin subestimación:")
print("SE ESPERA LA RUTA: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] ==> 101 + 97 + 80 + 140 = 418")
print(search.bab(ab).path())
print("-------------------------------------------------------------------------------------------------------")
print("Ramificación y salto con subestimación:")
print(search.bab_sub(ab).path())
print("-------------------------------------------------------------------------------------------------------")

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450