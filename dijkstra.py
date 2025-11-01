"""
MIT License

Copyright (c) 2024 Maarten-de-Groot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import heapq
from typing import Dict, List, Tuple

def dijkstra(graph: Dict[str, Dict[str, float]], start: str) -> Dict[str, float]:
    """
    Implementatie van Dijkstra's algoritme om de kortste afstand van een startnode
    naar alle andere nodes in een gewogen grafiek te vinden. De gewichten in de grafiek
    vertegenwoordigen de afstanden tussen de nodes.

    Parameters:
    graph (dict): Een grafiek weergegeven als een dictionary waarbij elke node
                  een dictionary van buren en hun respectievelijke afstanden bevat.
    start (str): De startnode in de grafiek.

    Returns:
    dict: Een dictionary met de kortste afstand van de startnode naar elke andere node.
    """
    # Input validatie
    if not graph:
        raise ValueError("Grafiek mag niet leeg zijn.")
    if not isinstance(start, str):
        raise TypeError("Startnode moet een string zijn.")
    if start not in graph:
        raise ValueError(f"Startnode '{start}' bestaat niet in de grafiek.")

    # Valideer dat alle gewichten numeriek en niet-negatief zijn
    for node_key, neighbors in graph.items():
        if not isinstance(neighbors, dict):
            raise TypeError(f"Neighbors van node '{node_key}' moeten een dictionary zijn.")
        for neighbor_key, edge_weight in neighbors.items():
            if not isinstance(edge_weight, (int, float)):
                msg = f"Gewicht van '{node_key}' naar '{neighbor_key}' moet numeriek zijn."
                raise TypeError(msg)
            if edge_weight < 0:
                msg = (f"Gewicht van '{node_key}' naar '{neighbor_key}' mag niet negatief zijn "
                       "(Dijkstra vereist niet-negatieve gewichten).")
                raise ValueError(msg)

    # Initialiseer alle afstanden als oneindig en stel de afstand naar de startnode in op 0
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Maak een prioriteitswachtrij (heap) om nodes in volgorde van hun afstand te bewaren
    queue = [(0, start)]
    visited = set()  # Houdt bij welke nodes we al hebben verwerkt

    # Zolang de wachtrij niet leeg is, blijven we de nodes bezoeken
    while queue:
        # Haal de node met de kleinste afstand uit de wachtrij
        current_distance, current_node = heapq.heappop(queue)

        # Sla deze node over als we hem al hebben verwerkt
        if current_node in visited:
            continue

        # Markeer deze node als bezocht
        visited.add(current_node)

        # Verken elke buur (neighbor) van de huidige node
        for neighbor, weight in graph[current_node].items():
            # Bereken de afstand van de huidige node naar deze buur
            new_distance = current_distance + weight

            # Als deze afstand kleiner is, update dan de afstand
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                # Voeg de buur toe aan de wachtrij voor verdere verkenning
                heapq.heappush(queue, (new_distance, neighbor))

    return distances

def dijkstra_shortest_path_to_end_nodes(
    graph: Dict[str, Dict[str, float]], start: str, ends: List[str]
) -> Tuple[float, List[str]]:
    """
    Vindt de beste (kortste) afstand en pad naar één of meerdere eindnodes.

    Deze functie breidt Dijkstra's algoritme uit om niet alleen de kortste afstand
    van de startnode naar alle andere nodes te vinden, maar ook om direct het
    kortste pad naar een specifieke set van eindnodes te identificeren. Dit is
    nuttig in scenario's waarbij meerdere bestemmingen mogelijk zijn en de kortste
    route naar de dichtstbijzijnde bestemming gewenst is.

    Parameters:
    - graph (dict): Een dictionary die de grafiek voorstelt, waarbij elke
                    node mapeert naar een dictionary van buren met hun respectievelijke
                    afstanden.
    - start (str): De startnode vanwaar het zoeken begint.
    - ends (list): Een lijst van eindnodes waarvoor het kortste pad gezocht wordt.

    Returns:
    - tuple: Een tuple bestaande uit de kortste afstand tot de dichtstbijzijnde
             eindnode en de lijst van nodes die het pad vormen.

    Raises:
    - ValueError: Als de grafiek leeg is, de startnode niet bestaat, of eindnodes
                   niet in de grafiek voorkomen.
    - TypeError: Als de input types incorrect zijn.
    """
    # Input validatie
    if not graph:
        raise ValueError("Grafiek mag niet leeg zijn.")
    if not isinstance(start, str):
        raise TypeError("Startnode moet een string zijn.")
    if not isinstance(ends, list):
        raise TypeError("Eindnodes moeten een lijst zijn.")
    if not ends:
        raise ValueError("Eindnodes lijst mag niet leeg zijn.")
    if start not in graph:
        raise ValueError(f"Startnode '{start}' bestaat niet in de grafiek.")

    # Valideer dat alle eindnodes in de grafiek voorkomen
    for end_node in ends:
        if end_node not in graph:
            raise ValueError(f"Eindnode '{end_node}' bestaat niet in de grafiek.")

    # Valideer dat alle gewichten numeriek en niet-negatief zijn
    for node_key, neighbors in graph.items():
        if not isinstance(neighbors, dict):
            raise TypeError(f"Neighbors van node '{node_key}' moeten een dictionary zijn.")
        for neighbor_key, edge_weight in neighbors.items():
            if not isinstance(edge_weight, (int, float)):
                msg = f"Gewicht van '{node_key}' naar '{neighbor_key}' moet numeriek zijn."
                raise TypeError(msg)
            if edge_weight < 0:
                msg = (f"Gewicht van '{node_key}' naar '{neighbor_key}' mag niet negatief zijn "
                       "(Dijkstra vereist niet-negatieve gewichten).")
                raise ValueError(msg)

    # Initialiseer afstanden naar alle nodes als oneindig
    result_distances = {node_key: float('infinity') for node_key in graph}
    # Houdt de voorganger van elke node bij voor padreconstructie
    previous_nodes = {node_key: None for node_key in graph}
    result_distances[start] = 0

    # Gebruik een prioriteitswachtrij om nodes te verwerken
    queue = [(0, start)]
    reached_ends = {}  # Houdt bereikte eindnodes bij met hun afstand

    # Blijf de queue verwerken tot deze leeg is of alle eindnodes zijn bereikt
    visited_nodes = set()  # Houdt bij welke nodes we al hebben verwerkt

    while queue and len(reached_ends) < len(ends):
        # Haal de node met de kleinste afstand uit de queue
        curr_dist, curr_node = heapq.heappop(queue)

        # Sla deze node over als we hem al hebben verwerkt
        if curr_node in visited_nodes:
            continue

        # Markeer deze node als bezocht
        visited_nodes.add(curr_node)

        # Als de huidige node een van de eindnodes is, sla deze op
        if curr_node in ends:
            reached_ends[curr_node] = curr_dist

        # Update afstanden naar buren als een kortere weg gevonden is
        for neighbor_key, edge_weight in graph[curr_node].items():
            # Nieuwe potentiële afstand tot buur
            new_dist = curr_dist + edge_weight

            # Als de nieuwe afstand korter is, update en voeg de buur toe
            if new_dist < result_distances[neighbor_key]:
                result_distances[neighbor_key] = new_dist
                # Update voorganger voor padreconstructie
                previous_nodes[neighbor_key] = curr_node
                # Voeg buur toe met nieuwe afstand
                heapq.heappush(queue, (new_dist, neighbor_key))

    # Als geen van de eindnodes bereikt kon worden, raise een exception
    if not reached_ends:
        raise ValueError("Geen van de eindnodes is bereikbaar vanuit het startpunt.")

    # Vind de dichtstbijzijnde eindnode met de kortste afstand
    best_end = min(reached_ends, key=reached_ends.get)

    # Reconstructeer het pad naar de dichtstbijzijnde eindnode
    result_path = []
    path_node = best_end
    while path_node is not None:
        # Voeg de huidige node toe aan het begin van het pad
        result_path.insert(0, path_node)
        # Ga terug naar de voorganger
        path_node = previous_nodes[path_node]

    # Retourneer de kortste afstand en het gereconstrueerde pad
    return (reached_ends[best_end], result_path)

if __name__ == "__main__":
    # Demonstratie van het gebruik
    demo_graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    print("Demonstratie van Dijkstra's algoritme:")
    print(f"Grafiek: {demo_graph}")
    print()

    # Test dijkstra functie
    print("Alle kortste afstanden vanaf 'A':")
    all_distances = dijkstra(demo_graph, 'A')
    for demo_node, demo_dist in all_distances.items():
        print(f"  Van A naar {demo_node}: {demo_dist}")
    print()

    # Test dijkstra_shortest_path_to_end_nodes functie
    print("Kortste pad van 'A' naar ['C', 'D']:")
    demo_distance, demo_path = dijkstra_shortest_path_to_end_nodes(
        demo_graph, 'A', ['C', 'D']
    )
    print(f"  Afstand: {demo_distance}")
    print(f"  Pad: {' -> '.join(demo_path)}")
    print()
    print("Tip: Gebruik test_dijkstra.py voor uitgebreide unit tests.")
