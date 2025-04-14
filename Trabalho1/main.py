grafo = {
    "Foz do Iguaçu": [("Cascavel", 125)], #Check
    "Cascavel": [("Foz do Iguaçu", 125), ("Campo Mourão", 150), ("Guarapuava", 200)], #Check
    "Campo Mourão": [("Cascavel", 150), ("Maringá", 90), ("Guarapuava", 175)], #Check
    "Maringá": [("Campo Mourão", 90), ("Mandaguari", 35)], #Check
    "Mandaguari": [("Maringá", 35), ("Arapongas", 25), ("Jandaia do Sul", 10)], #Check  
    "Arapongas": [("Mandaguari", 25), ("Apucarana", 20), ("Londrina", 30)], #Check
    "Apucarana": [("Arapongas", 20), ("Jandaia do Sul", 20), ("Ponta Grossa", 205)],#Check
    "Jandaia do Sul": [("Apucarana", 20), ("Mandaguari", 10), ("Guarapuava", 220)], #Check
    "Guarapuava": [("Jandaia do Sul", 220), ("Cascavel", 200), ("Irati", 90), ("Ponta Grossa", 150), ("Campo Mourão", 175)], #Check
    "Irati": [("Guarapuava", 90), ("Curitiba", 135)],#Check
    "Curitiba": [("Irati", 135), ("Ponta Grossa", 110)],#Check
    "Ponta Grossa": [("Curitiba", 110), ("Guarapuava", 150), ("Apucarana", 205), ("Ourinhos", 275)], #Check
    "Ourinhos": [("Ponta Grossa", 275), ("Londrina", 125)], #Check
    "Londrina": [("Ourinhos", 125), ("Arapongas", 30)] #Check
}

#Heuristica Partindo de Curitiba
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

caminho, custo = a_estrela("Curitiba", "Campo Mourão")
print("Melhor caminho:", caminho)
print("Custo total:", custo)
