# Search methods

import search
print("Prueba 1 de A a B")
ab = search.GPSProblem('A', 'B'
                       , search.romania)

print("Breadth_First:",search.breadth_first_graph_search(ab).path())
print("Depth_First: ",search.depth_first_graph_search(ab).path())
print("Recorrido y profundidad: ",search.recorrido_y_profundidad(ab).path())
print("Recorrido y profundidad con subestimación: ",search.recorrido_y_profundidad_subestimacion(ab).path())
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
print("\nPrueba 2 de I a B")
ib = search.GPSProblem('I', 'B'
                       , search.romania)

print("Breadth_First:",search.breadth_first_graph_search(ib).path())
print("Depth_First: ",search.depth_first_graph_search(ib).path())
print("Recorrido y profundidad: ",search.recorrido_y_profundidad(ib).path())
print("Recorrido y profundidad con subestimación: ",search.recorrido_y_profundidad_subestimacion(ib).path())

print("\nPrueba 3 de C a B")
cb = search.GPSProblem('C', 'B'
                       , search.romania)

print("Breadth_First:",search.breadth_first_graph_search(cb).path())
print("Depth_First: ",search.depth_first_graph_search(cb).path())
print("Recorrido y profundidad: ",search.recorrido_y_profundidad(cb).path())
print("Recorrido y profundidad con subestimación: ",search.recorrido_y_profundidad_subestimacion(cb).path())

print("\nPrueba 4 de U a B")
ub = search.GPSProblem('U', 'B'
                       , search.romania)

print("Breadth_First:",search.breadth_first_graph_search(ub).path())
print("Depth_First: ",search.depth_first_graph_search(ub).path())
print("Recorrido y profundidad: ",search.recorrido_y_profundidad(ub).path())
print("Recorrido y profundidad con subestimación: ",search.recorrido_y_profundidad_subestimacion(ub).path())

print("\nPrueba 5 de E a F")
ef = search.GPSProblem('E', 'F'
                       , search.romania)

print("Breadth_First:",search.breadth_first_graph_search(ef).path())
print("Depth_First: ",search.depth_first_graph_search(ef).path())
print("Recorrido y profundidad: ",search.recorrido_y_profundidad(ef).path())
print("Recorrido y profundidad con subestimación: ",search.recorrido_y_profundidad_subestimacion(ef).path())