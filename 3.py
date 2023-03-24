import xml.etree.ElementTree as ET
import xml.etree.ElementTree as ET
import json

with open(r"targetsist\dados.json", "r") as file:
    dados_faturamento = json.load(file)

for dado in dados_faturamento:
    dado['valor'] = float(dado['valor'])

tree = ET.parse(
    r'targetsist\dados (2).xml')
root = tree.getroot()

for child in root:
    if child.text.strip() and float(child.text) not in dados_faturamento:
        dados_faturamento.append(float(child.text))

faturamento_valido = [fatur['valor']
                      for fatur in dados_faturamento if fatur['valor'] != 0]
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)
