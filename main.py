print("Seja bem-vindo ao Algoritmo de Cálculo de Score do LASSI")

from banco_de_questoes import (
    questoesAtitude, questoesMotivacao, questoesOrgDeTempo,
    questoesAnsiedade, questoesConcentracao, questoesProcDeInformacoes,
    questoesSelecaoDeIdeias, questoesAuxDeEstudo, questoesAutoverificacao,
    questoesEstDeVerificacao, questoesNegativas
)

# Respostas do usuário
respostas = [1,	4,	4,	1,	5,	5,	3,	5,	1,	4,	2,	3,	3,	1,	3,	2,	3,	5,	4,	3,	1,	2,	4,	5,	4,	5,	3,	5,	3,	5,	1,	3,	4,	3,	4,	5,	4,	3,	3,	4,	5,	5,	5,	4,	5,	5,	5,	4,	5,	3,	4,	4,	3,	5,	5,	5,	5,	5,	3,	5,	5,	1,	5,	5,	1,	5,	4,	5,	5,	1,	3,	4,	3,	1,	1,	3,	1]  # Lista para armazenar as 77 respostas

# Função para atribuir valores às categorias
def atribuir_valores():
    todas_questoes = {
        'Atitude': questoesAtitude,
        'Motivação': questoesMotivacao,
        'Organização de Tempo': questoesOrgDeTempo,
        'Ansiedade': questoesAnsiedade,
        'Concentração': questoesConcentracao,
        'Processamento de Informações': questoesProcDeInformacoes,
        'Seleção de Ideias': questoesSelecaoDeIdeias,
        'Auxílio de Estudo': questoesAuxDeEstudo,
        'Autoverificação': questoesAutoverificacao,
        'Estudo de Verificação': questoesEstDeVerificacao
    }

    valores_atribuidos = {}
    indice_resposta = 0

    # Atribuindo valores às questões
    for categoria, questoes in todas_questoes.items():
        valores_atribuidos[categoria] = []
        for questao in questoes:
            valor = respostas[indice_resposta]  # Pega o valor da lista de respostas
            indice_resposta += 1
            valores_atribuidos[categoria].append((questao, valor))
    
    # Atualiza as questões negativas
    for categoria, questoes in valores_atribuidos.items():
        for i, (questao, valor) in enumerate(questoes):
            if questao in questoesNegativas:  # Verifica se a questão está na lista de negativas
                questoes[i] = (questao, inverter_valores(valor))  # Inverte o valor
    
    return valores_atribuidos

# Função para inverter os valores
def inverter_valores(valor):
    if valor == 1:
        return 5
    elif valor == 2:
        return 4
    elif valor == 3:
        return 3
    elif valor == 4:
        return 2
    elif valor == 5:
        return 1
    return valor  # Se o valor não for entre 1 e 5, retorna o valor original

# Função para calcular o score por categoria
def calcular_score(valores_atribuidos):
    scores = {}
    total_score = 0
    total_questoes = 0

    for categoria, questoes in valores_atribuidos.items():
        soma_categoria = sum(valor for _, valor in questoes)
        total_categoria = len(questoes) * 5  # Máximo possível por questão é 5
        score_categoria = (soma_categoria / total_categoria) * 10  # Normaliza para escala de 0 a 10
        scores[categoria] = score_categoria
        total_score += soma_categoria
        total_questoes += len(questoes)
    
    # Calcula o score geral
    score_geral = (total_score / (total_questoes * 5)) * 10  # Normaliza para escala de 0 a 10
    return scores, score_geral

# Função para exibir os scores
def exibir_scores(scores, score_geral):
    print("\nScores por Categoria:")
    for categoria, score in scores.items():
        print(f"{categoria}: {score:.2f}")
    print(f"\nScore Geral: {score_geral:.2f}")

# Execução do código
valores = atribuir_valores()
scores, score_geral = calcular_score(valores)
exibir_scores(scores, score_geral)
