# OBJETIVO: Allanar un terreno.

Sea un terreno `T`  de dimensiones `CxF` `([0..C-1] x [0..F-1])`, en cuyas casillas puede haber una cantidad de arena no mayor que una cantidad `MAX`, y un pequeño tractor en una casilla `(xr,yr)` determinada. 

La acción asociada al tractor es la distribución de una cantidad de arena  `S` de su casilla entre las casillas adyacentes (norte, sur, este y oeste) y el desplazamiento a alguna de ellas. Cada acción que el tractor realiza tiene un costo energético equivalente a la cantidad mayor de arena que ha de trasladar entre dos casillas.
