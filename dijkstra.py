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
    if start not in graph:
        return "Startnode bestaat niet in de grafiek."
    
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

def find_best_path_and_distance_to_ends(graph, start, ends):
    """
    Vindt de beste (kortste) afstand en pad naar één of meerdere eindnodes.
    
    Deze functie breidt Dijkstra's algoritme uit om niet alleen de kortste afstand van de startnode naar alle andere nodes te vinden,
    maar ook om direct het kortste pad naar een specifieke set van eindnodes te identificeren. Dit is nuttig in scenario's waarbij
    meerdere bestemmingen mogelijk zijn en de kortste route naar de dichtstbijzijnde bestemming gewenst is.

    Parameters:
    - graph (dict): Een dictionary die de grafiek voorstelt, waarbij elke node mapeert naar een dictionary van buren met hun respectievelijke afstanden.
    - start (str): De startnode vanwaar het zoeken begint.
    - ends (list): Een lijst van eindnodes waarvoor het kortste pad gezocht wordt.

    Returns:
    - tuple: Een tuple bestaande uit de kortste afstand tot de dichtstbijzijnde eindnode en de lijst van nodes die het pad vormen.
    """
    # Initialiseer afstanden naar alle nodes als oneindig en zet de afstand naar de startnode op 0
    distances = {node: float('infinity') for node in graph}
    previous_nodes = {node: None for node in graph}  # Houdt de voorganger van elke node bij voor padreconstructie
    distances[start] = 0
    
    # Gebruik een prioriteitswachtrij om nodes te verwerken in volgorde van hun huidige kortste afstand
    queue = [(0, start)]
    reached_ends = {}  # Houdt bereikte eindnodes bij met hun afstand
    
    # Blijf de queue verwerken tot deze leeg is of alle eindnodes zijn bereikt
    while queue and len(reached_ends) < len(ends):
        current_distance, current_node = heapq.heappop(queue)  # Haal de node met de kleinste afstand uit de queue
        
        # Als de huidige node een van de eindnodes is, sla deze op in reached_ends
        if current_node in ends:
            reached_ends[current_node] = current_distance
        
        # Update afstanden naar buren als een kortere weg gevonden is
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight  # Nieuwe potentiële afstand tot buur
            
            # Als de nieuwe afstand korter is, update en voeg de buur toe aan de queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node  # Update voorganger voor padreconstructie
                heapq.heappush(queue, (distance, neighbor))  # Voeg buur toe met nieuwe afstand
                
    # Als geen van de eindnodes bereikt kon worden, retourneer een foutmelding
    if not reached_ends:
        return ("Geen van de eindnodes is bereikbaar.", [])
        
    # Vind de dichtstbijzijnde eindnode met de kortste afstand
    best_end = min(reached_ends, key=reached_ends.get)
    
    # Reconstructeer het pad naar de dichtstbijzijnde eindnode
    path = []
    current_node = best_end
    while current_node is not None:
        path.insert(0, current_node)  # Voeg de huidige node toe aan het begin van het pad
        current_node = previous_nodes[current_node]  # Ga terug naar de voorganger
        
    # Retourneer de kortste afstand en het gereconstrueerde pad
    return (reached_ends[best_end], path)

# Unit tests functie om de correctheid van de find_best_path_and_distance_to_ends functie te verifiëren.
def run_tests():
    # Definieer een voorbeeldgrafiek als een dictionary. 
    # De sleutels zijn node-identificaties en de waarden zijn dictionaries 
    # die buren van elke node en de afstanden naar hen representeren.
    graph = {
        'A': {'B': 1, 'C': 4},  # Node 'A' is verbonden met 'B' (afstand 1) en 'C' (afstand 4)
        'B': {'A': 1, 'C': 2, 'D': 5},  # Node 'B' is verbonden met 'A', 'C', en 'D'
        'C': {'A': 4, 'B': 2, 'D': 1},  # Node 'C' is verbonden met 'A', 'B', en 'D'
        'D': {'B': 5, 'C': 1}  # Node 'D' is verbonden met 'B' en 'C'
    }
    # Stel 'A' in als de startnode voor de test
    start = 'A'
    # Definieer de eindnodes voor deze specifieke test
    ends = ['D', 'C']  # Het doel is om de kortste route naar 'D' of 'C' te vinden

    # Stel verwachte resultaten in voor deze test:
    expected_distance = 3  # De verwachte kortste afstand van 'A' naar 'C' via 'B' is 3
    expected_path = ['A', 'B', 'C']  # Het verwachte pad van 'A' naar 'C' via 'B'

    # Roep de functie aan met de testdata en sla de resultaten op
    distance, path = find_best_path_and_distance_to_ends(graph, start, ends)
    
    # Voer de daadwerkelijke test uit: Vergelijk de verkregen resultaten met de verwachte resultaten
    assert distance == expected_distance, f"Verwachte afstand {expected_distance}, maar kreeg {distance}"
    assert path == expected_path, f"Verwacht pad {expected_path}, maar kreeg {path}"
    
    # Dit patroon van testen helpt bij het valideren van de correctheid van de algoritme-implementatie,
    # en zorgt ervoor dat toekomstige wijzigingen in de code de bestaande functionaliteit niet breken.

    # Als bovenstaande beweringen waar zijn (geen AssertionError wordt opgeworpen),
    # dan is de test geslaagd. Print een bevestiging.
    print("Alle tests geslaagd.")

if __name__ == "__main__":
    run_tests()
    print("Dit script demonstreert nu het gebruik van Dijkstra's algoritme met een voorbeeld.")
    print("Dit script is bedoeld om geïmporteerd te worden, niet om direct uitgevoerd te worden.")
