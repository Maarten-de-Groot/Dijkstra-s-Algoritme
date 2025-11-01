# Dijkstra's kortste pad algoritme in Python

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)

Welkom bij deze repository waarin we een toegankelijke implementatie van het Dijkstra-algoritme presenteren. Deze code is ontworpen om het kortste pad in een netwerk, zoals een gebouwenplattegrond of een stratenkaart, te vinden. We hebben geprobeerd alles zo duidelijk mogelijk uit te leggen, zodat iedereen, ongeacht hun programmeerervaring, het kan begrijpen en gebruiken.

## Inhoudsopgave
1. [Introductie](#introductie)
2. [Wat is Dijkstra's Algoritme?](#wat-is-dijkstras-algoritme)
3. [Hoe werkt onze Code?](#hoe-werkt-onze-code)
4. [Installatie](#installatie)
5. [Hoe gebruik je deze code?](#hoe-gebruik-je-deze-code)
6. [Functies](#functies)
7. [Error Handling](#error-handling)
8. [Voorbeelden](#voorbeelden)
9. [Licentie](#licentie)

## Introductie
Dijkstra's algoritme is een beroemde methode in de computertechniek om het kortste pad te vinden in een netwerk van verschillende punten (ook wel 'nodes' genoemd) en verbindingen (ook wel 'edges' genoemd). Onze implementatie in Python maakt dit algoritme toegankelijk voor allerlei toepassingen, van routeplanning tot netwerkanalyse.

## Wat is Dijkstra's Algoritme?
Dijkstra's algoritme is een manier om het kortste pad te vinden in een netwerk waar elk pad een bepaalde afstand of 'gewicht' heeft. Het kiest het pad dat de totale afstand van het startpunt naar het eindpunt minimaliseert.

## Hoe werkt onze code?
Onze code bestaat uit twee belangrijke delen:
1. **Het Dijkstra Algoritme**: Dit deel vindt de kortste afstand van een startpunt (node) naar alle andere punten in het netwerk.
2. **Zoekfunctie naar specifieke eindnodes**: Dit deel gebruikt het Dijkstra algoritme om het kortste pad naar een specifieke set van eindpunten te vinden.

## Installatie

Kopieer het `dijkstra.py` bestand naar je projectmap of clone deze repository:

```bash
git clone https://github.com/maarten-de-groot/Dijkstra-s-Algoritme.git
cd Dijkstra-s-Algoritme
```

**Vereisten**: Python 3.6 of hoger. Deze implementatie gebruikt alleen de standaardbibliotheek (`heapq` en `typing`).

## Hoe gebruik je deze code?

### Stap 1: Importeer de functies

```python
from dijkstra import dijkstra, dijkstra_shortest_path_to_end_nodes
```

### Stap 2: Definieer je netwerk (grafiek)

Je netwerk bestaat uit punten (nodes) en de afstanden tussen hen (edges). Hier is een voorbeeld:

```python
graph = {
    "A": {"B": 5, "C": 10},
    "B": {"A": 5, "D": 3},
    "C": {"A": 10, "D": 6},
    "D": {"B": 3, "C": 6}
}
```

In dit voorbeeld zijn `A`, `B`, `C`, en `D` de punten in je netwerk. De getallen representeren de afstand tussen deze punten. Bijvoorbeeld, de afstand van `A` naar `B` is `5`.

**Belangrijk**: 
- Gewichten moeten niet-negatief zijn (Dijkstra's algoritme werkt alleen met niet-negatieve gewichten)
- De grafiek kan gericht zijn (niet-symmetrisch) of ongericht (symmetrisch)

### Stap 3: Voer de code uit

**Optie A: Vind kortste pad naar specifieke eindnodes**

```python
start_node = 'A'
end_nodes = ['C', 'D']

shortest_distance, path = dijkstra_shortest_path_to_end_nodes(graph, start_node, end_nodes)
print(f"Kortste afstand: {shortest_distance}")
print(f"Pad: {' -> '.join(path)}")
```

**Optie B: Vind kortste afstanden naar alle nodes**

```python
start_node = 'A'
distances = dijkstra(graph, start_node)
print(distances)  # {'A': 0, 'B': 5, 'C': 10, 'D': 8}
```

## Functies

### `dijkstra(graph, start)`

Vindt de kortste afstand van een startnode naar alle andere nodes in de grafiek.

**Parameters:**
- `graph` (dict): Een dictionary waarbij elke node mapeert naar een dictionary van buren met hun respectievelijke afstanden
- `start` (str): De startnode

**Returns:**
- `dict`: Een dictionary met de kortste afstand van de startnode naar elke andere node

**Raises:**
- `ValueError`: Als de grafiek leeg is, de startnode niet bestaat, of gewichten negatief zijn
- `TypeError`: Als de input types incorrect zijn

### `dijkstra_shortest_path_to_end_nodes(graph, start, ends)`

Vindt het kortste pad naar één of meerdere eindnodes.

**Parameters:**
- `graph` (dict): Een dictionary die de grafiek voorstelt
- `start` (str): De startnode
- `ends` (list): Een lijst van eindnodes

**Returns:**
- `tuple`: Een tuple bestaande uit de kortste afstand (float) en de lijst van nodes die het pad vormen (list[str])

**Raises:**
- `ValueError`: Als de grafiek leeg is, de startnode/eindnodes niet bestaan, of geen eindnodes bereikbaar zijn
- `TypeError`: Als de input types incorrect zijn

## Error Handling

De functies gebruiken exceptions voor foutafhandeling in plaats van foutmeldingen te retourneren. Dit maakt de code robuuster en duidelijker:

```python
try:
    distance, path = dijkstra_shortest_path_to_end_nodes(graph, start, ends)
    print(f"Kortste pad: {path} met afstand {distance}")
except ValueError as e:
    print(f"Fout: {e}")
except TypeError as e:
    print(f"Type fout: {e}")
```

## Voorbeelden

### Voorbeeld 1: Eenvoudige routeplanning

```python
from dijkstra import dijkstra_shortest_path_to_end_nodes

# Steden en wegen tussen hen
cities = {
    "Amsterdam": {"Utrecht": 45, "Rotterdam": 75},
    "Utrecht": {"Amsterdam": 45, "Rotterdam": 60},
    "Rotterdam": {"Amsterdam": 75, "Utrecht": 60, "Den Haag": 25},
    "Den Haag": {"Rotterdam": 25}
}

start = "Amsterdam"
destinations = ["Den Haag", "Utrecht"]

distance, path = dijkstra_shortest_path_to_end_nodes(cities, start, destinations)
print(f"Kortste route van {start} naar {path[-1]}: {' -> '.join(path)} ({distance} km)")
# Output: Kortste route van Amsterdam naar Utrecht: Amsterdam -> Utrecht (45 km)
```

### Voorbeeld 2: Alle afstanden vinden

```python
from dijkstra import dijkstra

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1}
}

distances = dijkstra(graph, "A")
for node, distance in distances.items():
    print(f"Van A naar {node}: {distance}")
```

## Licentie
Dit project is beschikbaar onder de [MIT License](LICENSE).
