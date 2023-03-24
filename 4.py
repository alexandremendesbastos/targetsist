faturamento_mensal = {
    'sp': 67836.43,
    'rj': 36678.66,
    'mg': 29229.88,
    'es': 27165.48,
    'outros': 19849.53
}

total_faturamento = sum(faturamento_mensal.values())

representacao_percentual = {}

for estado, faturamento in faturamento_mensal.items():
    representacao_percentual[estado] = (faturamento / total_faturamento) * 100


for estado, representacao in representacao_percentual.items():
    print(f"{estado}: {representacao:.2f}%")
