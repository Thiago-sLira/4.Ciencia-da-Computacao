from conteudo import Conjunto

estudantes = [1, 2, 3, 4, 5, 6, 7]
lista1_entregues = [1, 4, 7, 3]
lista2_entregues = [3, 1, 6]

conjuntoEstudantes = Conjunto()
conjuntoLista1 = Conjunto()
conjuntoLista2 = Conjunto()

for estudante in estudantes:
    conjuntoEstudantes.add(estudante)

for lista1 in lista1_entregues:
    conjuntoLista1.add(lista1)

for lista2 in lista2_entregues:
    conjuntoLista2.add(lista2)

print(
    conjuntoEstudantes.difference(conjuntoLista1)
)  # Não entregaram a lista 1

print(conjuntoLista1.intersection(conjuntoLista2))  # Entregaram as duas listas

print(conjuntoLista1.union(conjuntoLista2))  # Entregou pelo ou menos uma lista

print(
    conjuntoEstudantes.difference(conjuntoLista1.union(conjuntoLista2))
)  # Entregaram as duas listas
