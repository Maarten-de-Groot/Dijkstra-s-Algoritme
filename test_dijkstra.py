"""
Unit tests voor de Dijkstra implementatie.
"""

import pytest
from dijkstra import dijkstra, dijkstra_shortest_path_to_end_nodes


def test_dijkstra_basic():
    """Test de basis functionaliteit van het dijkstra algoritme."""
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    distances = dijkstra(graph, 'A')
    assert distances['A'] == 0
    assert distances['B'] == 1
    assert distances['C'] == 3  # A -> B -> C (1 + 2 = 3)
    assert distances['D'] == 4  # A -> B -> C -> D (1 + 2 + 1 = 4)


def test_dijkstra_shortest_path_to_end_nodes():
    """Test de kortste pad functie naar eindnodes."""
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    start = 'A'
    ends = ['D', 'C']
    
    distance, path = dijkstra_shortest_path_to_end_nodes(graph, start, ends)
    
    assert distance == 3  # A -> B -> C (1 + 2 = 3)
    assert path == ['A', 'B', 'C']


def test_dijkstra_single_end_node():
    """Test met één eindnode."""
    graph = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'D': 3},
        'C': {'A': 10, 'D': 6},
        'D': {'B': 3, 'C': 6}
    }
    distance, path = dijkstra_shortest_path_to_end_nodes(graph, 'A', ['D'])
    assert distance == 8  # A -> B -> D (5 + 3 = 8)
    assert path == ['A', 'B', 'D']


def test_dijkstra_start_not_in_graph():
    """Test dat een ValueError wordt gegooid als startnode niet bestaat."""
    graph = {'A': {'B': 1}, 'B': {'A': 1}}
    with pytest.raises(ValueError, match="Startnode 'C' bestaat niet"):
        dijkstra(graph, 'C')


def test_dijkstra_empty_graph():
    """Test dat een ValueError wordt gegooid voor lege grafiek."""
    with pytest.raises(ValueError, match="Grafiek mag niet leeg zijn"):
        dijkstra({}, 'A')


def test_dijkstra_negative_weights():
    """Test dat negatieve gewichten worden afgevangen."""
    graph = {'A': {'B': -1}, 'B': {'A': -1}}
    with pytest.raises(ValueError, match="mag niet negatief zijn"):
        dijkstra(graph, 'A')


def test_dijkstra_shortest_path_unreachable():
    """Test dat een ValueError wordt gegooid als eindnodes niet bereikbaar zijn."""
    graph = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {'D': 1},
        'D': {'C': 1}
    }
    with pytest.raises(ValueError, match="Geen van de eindnodes is bereikbaar"):
        dijkstra_shortest_path_to_end_nodes(graph, 'A', ['C'])


def test_dijkstra_shortest_path_empty_ends():
    """Test dat een ValueError wordt gegooid voor lege eindnodes lijst."""
    graph = {'A': {'B': 1}, 'B': {'A': 1}}
    with pytest.raises(ValueError, match="Eindnodes lijst mag niet leeg zijn"):
        dijkstra_shortest_path_to_end_nodes(graph, 'A', [])


def test_dijkstra_type_error():
    """Test dat TypeError wordt gegooid voor verkeerde types."""
    graph = {'A': {'B': 1}}
    with pytest.raises(TypeError, match="Startnode moet een string zijn"):
        dijkstra(graph, 123)


if __name__ == "__main__":
    # Voor het geval pytest niet geïnstalleerd is, voer basis tests uit
    try:
        pytest.main([__file__, "-v"])
    except ImportError:
        print("pytest is niet geïnstalleerd. Installeer het met: pip install pytest")
        print("Voer handmatige tests uit:")
        
        # Basis test zonder pytest
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }
        start = 'A'
        ends = ['D', 'C']
        
        distance, path = dijkstra_shortest_path_to_end_nodes(graph, start, ends)
        assert distance == 3, f"Verwachte afstand 3, maar kreeg {distance}"
        assert path == ['A', 'B', 'C'], f"Verwacht pad ['A', 'B', 'C'], maar kreeg {path}"
        
        print("✓ Basis test geslaagd!")

