grafo = {
    "Foz do Iguaçu": [("Cascavel", 125)],
    "Cascavel": [("Foz do Iguaçu", 125), ("Campo Mourão", 130), ("Guarapuava", 200)],
    "Campo Mourão": [("Cascavel", 130), ("Maringá", 90)],
    "Maringá": [("Campo Mourão", 90), ("Mandaguari", 35)],
    "Mandaguari": [("Maringá", 35), ("Arapongas", 25)],
    "Arapongas": [("Mandaguari", 25), ("Apucarana", 20), ("Londrina", 30)],
    "Apucarana": [("Arapongas", 20), ("Jandaia do Sul", 20), ("Ponta Grossa", 205)],
    "Jandaia do Sul": [("Apucarana", 20), ("Mandaguari", 10), ("Guarapuava", 220)],
    "Guarapuava": [("Jandaia do Sul", 220), ("Cascavel", 200), ("Irati", 90), ("Ponta Grossa", 150)],
    "Irati": [("Guarapuava", 90), ("Curitiba", 135)],
    "Curitiba": [("Irati", 135), ("Ponta Grossa", 110)],
    "Ponta Grossa": [("Curitiba", 110), ("Guarapuava", 150), ("Apucarana", 205), ("Ourinhos", 275)],
    "Ourinhos": [("Ponta Grossa", 275), ("Londrina", 125)],
    "Londrina": [("Ourinhos", 125), ("Arapongas", 30)]
}

heuristica = {  
    "Foz do Iguaçu": 400,
    "Cascavel": 320,
    "Campo Mourão": 290,
    "Maringá": 270,
    "Mandaguari": 260,
    "Arapongas": 240,
    "Apucarana": 230,
    "Jandaia do Sul": 220,
    "Guarapuava": 150,
    "Irati": 100,
    "Curitiba": 0,
    "Ponta Grossa": 80,
    "Ourinhos": 200,
    "Londrina": 210
}

import heapq

def a_estrela(inicio, objetivo):
    fila = []
    heapq.heappush(fila, (0 + heuristica[inicio], 0, inicio, [inicio]))
    visitados = set()

    while fila:
        f, g, atual, caminho = heapq.heappop(fila)
        if atual in visitados:
            continue
        visitados.add(atual)

        if atual == objetivo:
            return caminho, g

        for vizinho, custo in grafo[atual]:
            if vizinho not in visitados:
                novo_g = g + custo
                novo_f = novo_g + heuristica[vizinho]
                heapq.heappush(fila, (novo_f, novo_g, vizinho, caminho + [vizinho]))

    return None, float('inf')

caminho, custo = a_estrela("Ourinhos", "Jandaia do Sul")
print("Melhor caminho:", caminho)
print("Custo total:", custo)
