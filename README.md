
# Dijkstra's Kortste Pad Algoritme in Python

Welkom bij deze repository waarin we een toegankelijke implementatie van het Dijkstra-algoritme presenteren. Deze code is ontworpen om het kortste pad in een netwerk, zoals een gebouwenplattegrond of een stratenkaart, te vinden. We hebben geprobeerd alles zo duidelijk mogelijk uit te leggen, zodat iedereen, ongeacht hun programmeerervaring, het kan begrijpen en gebruiken.

## Inhoudsopgave
1. [Introductie](#introductie)
2. [Wat is Dijkstra's Algoritme?](#wat-is-dijkstras-algoritme)
3. [Hoe Werkt Onze Code?](#hoe-werkt-onze-code)
4. [Hoe Gebruik Je Deze Code?](#hoe-gebruik-je-deze-code)
5. [Bijdragen](#bijdragen)
6. [Licentie](#licentie)

## Introductie
Dijkstra's algoritme is een beroemde methode in de computertechniek om het kortste pad te vinden in een netwerk van verschillende punten (ook wel 'nodes' genoemd) en verbindingen (ook wel 'edges' genoemd). Onze implementatie in Python maakt dit algoritme toegankelijk voor allerlei toepassingen, van routeplanning tot netwerkanalyse.

## Wat is Dijkstra's Algoritme?
Dijkstra's algoritme is een manier om het kortste pad te vinden in een netwerk waar elk pad een bepaalde afstand of 'gewicht' heeft. Het kiest het pad dat de totale afstand van het startpunt naar het eindpunt minimaliseert.

## Hoe Werkt Onze Code?
Onze code bestaat uit twee belangrijke delen:
1. **Het Dijkstra Algoritme**: Dit deel vindt de kortste afstand van een startpunt (node) naar alle andere punten in het netwerk.
2. **Zoekfunctie naar Specifieke Eindnodes**: Dit deel gebruikt het Dijkstra algoritme om het kortste pad naar een specifieke set van eindpunten te vinden.

## Hoe Gebruik Je Deze Code?
### Stap 1: Definieer Je Netwerk
Je netwerk bestaat uit punten (nodes) en de afstanden tussen hen (edges). Hier is een voorbeeld van hoe je dit kunt definiëren:

```python
graph = {
    "A": {"B": 5, "C": 10},
    "B": {"A": 5, "D": 3},
    "C": {"A": 10, "D": 6},
    "D": {"B": 3, "C": 6}
}
```

In dit voorbeeld zijn `A`, `B`, `C`, en `D` de punten in je netwerk. De getallen representeren de afstand tussen deze punten. Bijvoorbeeld, de afstand van `A` naar `B` is `5`.

### Stap 2: Bepaal je Startpunt en Eindpunten
Kies een startpunt van waaruit je het kortste pad wilt vinden. Bepaal ook je eindpunten. Bijvoorbeeld:

- Startpunt: `"A"`
- Eindpunten: `["C", "D"]`

### Stap 3: Voer de Code Uit
Gebruik de code om het kortste pad te vinden. De code zal het kortste pad van je startpunt naar elk eindpunt berekenen.

## Bijdragen
Jouw bijdragen maken dit project beter! Voel je vrij om bij te dragen door issues te openen of pull requests in te dienen.

## Licentie
Dit project is beschikbaar onder de [MIT License](LICENSE).
