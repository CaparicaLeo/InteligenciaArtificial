import heapq

grafo = {
    "Foz do Iguaçu": [("Cascavel", 125)],
    "Cascavel": [("Foz do Iguaçu", 125), ("Campo Mourão", 150), ("Guarapuava", 200)],
    "Campo Mourão": [("Cascavel", 150), ("Maringá", 90), ("Guarapuava", 175)],
    "Maringá": [("Campo Mourão", 90), ("Mandaguari", 35)],
    "Mandaguari": [("Maringá", 35), ("Arapongas", 25), ("Jandaia do Sul", 10)],
    "Arapongas": [("Mandaguari", 25), ("Apucarana", 20), ("Londrina", 30)],
    "Apucarana": [("Arapongas", 20), ("Jandaia do Sul", 20), ("Ponta Grossa", 205)],
    "Jandaia do Sul": [("Apucarana", 20), ("Mandaguari", 10), ("Guarapuava", 220)],
    "Guarapuava": [("Jandaia do Sul", 220), ("Cascavel", 200), ("Irati", 90), ("Ponta Grossa", 150), ("Campo Mourão", 175)],
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

def a_estrela(inicio, objetivo):
    fila = []
    heapq.heappush(fila, (heuristica[inicio], 0, inicio, [inicio]))
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

def main():
    print("==== CIDADES DISPONÍVEIS ====")
    for cidade in grafo.keys():
        print(" -", cidade)

    print("\n== DIGITE OS NOMES DAS CIDADES EXATAMENTE COMO ACIMA ==")
    partida = input("\nCidade de partida: ").strip()
    parada = input("Cidade de parada intermediária: ").strip()
    chegada = input("Cidade de destino final: ").strip()

    if partida not in grafo:
        print(f"\n[ERRO] Cidade de partida '{partida}' não encontrada.")
        return
    if parada not in grafo:
        print(f"\n[ERRO] Cidade de parada '{parada}' não encontrada.")
        return
    if chegada not in grafo:
        print(f"\n[ERRO] Cidade de destino '{chegada}' não encontrada.")
        return

    caminho1, custo1 = a_estrela(partida, parada)
    caminho2, custo2 = a_estrela(parada, chegada)

    if caminho1 and caminho2:
        # Remover duplicidade da parada se ela aparecer duas vezes
        caminho_completo = caminho1 + caminho2[1:] if caminho1[-1] == caminho2[0] else caminho1 + caminho2
        custo_total = custo1 + custo2

        print("\n==== ROTA CALCULADA ====")
        print("Caminho: ", " → ".join(caminho_completo))
        print(f"Custo total estimado: {custo_total} km")
        print("=========================")
    else:
        print("\n[ERRO] Não foi possível encontrar um caminho entre as cidades informadas.")


main()
