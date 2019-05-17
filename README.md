# practica1_tsi_search_algorithms

## Branch and bound.

Para la búsqueda branch and bound creamos una clase que representa a una cola a partir del código de la clase FifoQueue utilizada en la busqueda en amplitud.
En esta cola, cuando se van a añadir nuevos estados, se ordenan de menor a mayor según el coste —la sumatoria del coste de las aristas entre nodos/cuidades (la distancia) desde la ciudad inicial hasta la solución añadida a la solución que se está probando—.
Para ordenar los estados, se utiliza la función sorted de Python, que ordena una lista según una clave (en este caso el valor que retorna una función lambda que le pasamos, que devuelve el coste del estado actual).

## Branch and bound con heurística.

Para esta búsqueda se siguen los mismos pasos descritos anteriormente, pero ahora ordenando por la suma del coste del estado actual y de la heurística (evaluada mediante una función que ya tenemos implementada, la cual calcula la heurística para un estado del problema).
Tanto para esta búsqueda como para la anterior, y las ya implementadas en el código base, se ha introducido una variable más de resultado, la cual nos permite saber cuantos nodos han sido visitados. Para contabilizar el número de nodos visitados, añadimos un contador en el método graph_search, el cual cuenta el número de nodos sacados de la lista abierta — el número de estados visitados—. Esta cuenta la devolvemos junto al resultado (en la namedtuple Result).
