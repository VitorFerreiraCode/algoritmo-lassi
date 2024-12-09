from banco_de_questoes import (
    questoesAtitude, questoesMotivacao, questoesOrgDeTempo,
    questoesAnsiedade, questoesConcentracao, questoesProcDeInformacoes,
    questoesSelecaoDeIdeias, questoesAuxDeEstudo, questoesAutoverificacao,
    questoesEstDeVerificacao
)

# Junta todas as questões
todas_questoes = (
    questoesAtitude + questoesMotivacao + questoesOrgDeTempo +
    questoesAnsiedade + questoesConcentracao + questoesProcDeInformacoes +
    questoesSelecaoDeIdeias + questoesAuxDeEstudo + questoesAutoverificacao +
    questoesEstDeVerificacao
)

# Verifica se o total é 77
total_questoes = len(todas_questoes)
print(f"Total de questões: {total_questoes}")

# Verifica duplicatas
duplicatas = [questao for questao in set(todas_questoes) if todas_questoes.count(questao) > 1]

if duplicatas:
    print(f"Números duplicados encontrados: {duplicatas}")
else:
    print("Não há números duplicados.")

# Resultado final
if total_questoes == 77 and not duplicatas:
    print("Tudo está correto!")
else:
    print("Algo está errado.")
