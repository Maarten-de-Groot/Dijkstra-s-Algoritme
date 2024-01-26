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

def dijkstra(graph, start):
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
    # Initialiseer alle afstanden als oneindig en stel de afstand naar de startnode in op 0
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Maak een prioriteitswachtrij (heap) om nodes in volgorde van hun afstand te bewaren
    queue = [(0, start)]

    # Zolang de wachtrij niet leeg is, blijven we de nodes bezoeken
    while queue:
        # Haal de node met de kleinste afstand uit de wachtrij
        current_distance, current_node = heapq.heappop(queue)

        # Verken elke buur (neighbor) van de huidige node
        for neighbor, weight in graph[current_node].items():
            # Bereken de afstand van de huidige node naar deze buur
            distance = current_distance + weight

            # Als deze afstand kleiner is dan de reeds bekende afstand, update dan de afstand
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Voeg de buur toe aan de wachtrij voor verdere verkenning
                heapq.heappush(queue, (distance, neighbor))

    return distances

def dijkstra_shortest_path_to_end_nodes(graph, start, end_nodes):
    """
    Implementatie van Dijkstra's algoritme om de kortste afstand van een startnode
    naar een lijst van eindnodes te vinden.

    Parameters:
    graph (dict): Een grafiek weergegeven als een dictionary waarbij elke node
                  een dictionary van buren en hun respectievelijke afstanden bevat.
    start (str): De startnode in de grafiek.
    end_nodes (list): Een lijst van eindnodes.

    Returns:
    tuple: Een tuple met de dichtstbijzijnde eindnode en de kortste afstand daarnaartoe.
    """
    # Voer het standaard Dijkstra algoritme uit om afstanden naar alle nodes te vinden
    distances = dijkstra(graph, start)

    # Filter de resultaten om alleen de afstanden naar de eindnodes te tonen
    end_node_distances = {node: distances[node] for node in end_nodes if node in distances}

    # Vind de kortste afstand en bijbehorende node onder de eindnodes
    shortest_distance_node = min(end_node_distances, key=end_node_distances.get)
    shortest_distance = end_node_distances[shortest_distance_node]

    return shortest_distance_node, shortest_distance

def dijkstra_full_path(graph, start, end):
    """
    Implementatie van Dijkstra's algoritme om het volledige pad van startnode naar eindnode te vinden.

    Parameters:
    graph (dict): Een grafiek weergegeven als een dictionary waarbij elke node
                  een dictionary van buren en hun respectievelijke afstanden bevat.
    start (str): De startnode in de grafiek.
    end (str): De eindnode in de grafiek.

    Returns:
    list: Een lijst van nodes die het pad van start naar eind vormt.
    """
    distances = {node: float('infinity') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Als we de eindnode bereiken, stop dan
        if current_node == end:
            break

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Bouw het pad van eind naar start
    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]

    return path if path[0] == start else "Geen pad gevonden."

# Voorkom dat het script wordt uitgevoerd als het direct wordt aangeroepen
if __name__ == "__main__":
    print("Dit script is bedoeld om geïmporteerd te worden, niet om direct uitgevoerd te worden.")
